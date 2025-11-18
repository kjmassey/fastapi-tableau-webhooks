from fastapi import FastAPI, Request
import tableauserverclient as TSC
from fastapi.middleware.cors import CORSMiddleware
import dotenv
import os
from emails.send_email import send_email, generate_email_message, attach_pdf_to_email
from emails.admin_promoted import ADMIN_PROMOTED_EMAIL_BODY_HTML
from emails.datasource_created import DATASOURCE_CREATED_EMAIL_BODY_HTML
from emails.workbook_refresh_failed import WORKBOOK_REFRESH_FAILED_EMAIL_BODY_HTML
from emails.refresh_success_with_pdf import REFRESH_SUCCESS_WITH_PDF_EMAIL_BODY_HTML
from tableau.tableau_tsc import (
    get_user_by_luid,
    get_datasource_by_luid,
    get_workbook_by_luid,
    get_view_pdfs_by_workbook_luid,
)

app = FastAPI()

dotenv.load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/webhook")
async def tableau_webhook(request: Request):
    payload = await request.json()
    # Process the webhook payload as needed
    return {"status": "success", "data": payload}


@app.post("/admin-promoted")
async def admin_promoted(request: Request):
    payload = await request.json()

    user = get_user_by_luid(payload["resource_luid"])

    email_body = ADMIN_PROMOTED_EMAIL_BODY_HTML
    email_body = email_body.replace("[[SITE_NAME]]", os.environ.get("SITE_NAME"))
    email_body = email_body.replace("[[USER_NAME]]", user.name)
    email_body = email_body.replace("[[USER_ROLE]]", user.site_role)
    email_body = email_body.replace("[[EVENT_DATE]]", payload["created_at"])

    email_message = generate_email_message(email_body)
    send_email(email_message)
    return {"status": "success", "data": payload}


@app.post("/datasource-created")
async def datasource_created(request: Request):
    payload = await request.json()

    datasource = get_datasource_by_luid(payload["resource_luid"])
    publisher = get_user_by_luid(datasource.owner_id)

    email_body = DATASOURCE_CREATED_EMAIL_BODY_HTML
    email_body = email_body.replace("[[SITE_NAME]]", os.environ.get("SITE_NAME"))
    email_body = email_body.replace("[[DATASOURCE_NAME]]", datasource.name)
    email_body = email_body.replace("[[PUBLISHED_BY]]", publisher.name)
    email_body = email_body.replace("[[LINK]]", datasource.webpage_url)

    email_message = generate_email_message(email_body)
    send_email(email_message)
    return {"status": "success", "data": payload}


@app.post("/workbook-refresh-failed")
async def workbook_refresh_failed(request: Request):
    payload = await request.json()

    workbook = get_workbook_by_luid(payload["resource_luid"])
    publisher = get_user_by_luid(workbook.owner_id)

    email_body = WORKBOOK_REFRESH_FAILED_EMAIL_BODY_HTML
    email_body = email_body.replace("[[SITE_NAME]]", os.environ.get("SITE_NAME"))
    email_body = email_body.replace("[[WORKBOOK_NAME]]", workbook.name)
    email_body = email_body.replace("[[FAILURE_TIME]]", payload["created_at"])
    email_body = email_body.replace("[[OWNER]]", publisher.name)
    email_body = email_body.replace("[[LINK]]", workbook.webpage_url)

    email_message = generate_email_message(email_body)
    send_email(email_message)
    return {"status": "success", "data": payload}


@app.post("/refresh-success-with-pdf")
async def refresh_success_with_pdf(request: Request):
    payload = await request.json()

    workbook = get_workbook_by_luid(payload["resource_luid"])
    views_pdfs = get_view_pdfs_by_workbook_luid(payload["resource_luid"])
    publisher = get_user_by_luid(workbook.owner_id)

    email_body = REFRESH_SUCCESS_WITH_PDF_EMAIL_BODY_HTML
    email_body = email_body.replace("[[SITE_NAME]]", os.environ.get("SITE_NAME"))
    email_body = email_body.replace("[[WORKBOOK_NAME]]", workbook.name)
    email_body = email_body.replace("[[REFRESH_TIME]]", payload["created_at"])
    email_body = email_body.replace("[[LINK]]", workbook.webpage_url)
    email_body = email_body.replace("[[OWNER]]", publisher.name)
    email_body = email_body.replace("[[COMPLETED_AT]]", payload["created_at"])

    email_message = generate_email_message(email_body)

    for view in views_pdfs:
        attach_pdf_to_email(email_message, view["pdf"], f"{view['name']}.pdf")

    send_email(email_message)
    return {"status": "success", "data": payload}
