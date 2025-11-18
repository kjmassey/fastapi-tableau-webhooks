import tableauserverclient as TSC
import dotenv
import os

dotenv.load_dotenv()


def get_tableau_server_and_auth():
    """
    Retrieves/Configures the Tableau server and authentication object.
    """

    host = os.environ.get("HOST_ROOT")
    site_name = os.environ.get("SITE_NAME")
    pat_name = os.environ.get("PAT_NAME")
    pat_secret = os.environ.get("PAT_SECRET")
    api_version = os.environ.get("API_VERSION")

    tableau_auth = TSC.PersonalAccessTokenAuth(
        token_name=pat_name, personal_access_token=pat_secret, site_id=site_name
    )

    server = TSC.Server(host, use_server_version=True)
    server.version = api_version

    return server, tableau_auth


def get_all_users_on_site():
    """
    Retrieves all users on the Tableau site.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        all_users = list(TSC.Pager(server.users))

        return all_users


def get_user_by_luid(luid):
    """
    Retrieves a user by their LUID.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        tsc_user = server.users.get_by_id(luid)

        return tsc_user


def get_datasource_by_luid(luid):
    """
    Retrieves a datasource by its LUID.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        tsc_datasource = server.datasources.get_by_id(luid)

        return tsc_datasource


def get_all_workbooks_on_site():
    """
    Retrieves all workbooks on the Tableau site.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        all_workbooks = list(TSC.Pager(server.workbooks))

        return all_workbooks


def get_workbook_by_luid(luid):
    """
    Retrieves a workbook by its LUID.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        tsc_workbook = server.workbooks.get_by_id(luid)

        return tsc_workbook


def get_view_pdfs_by_workbook_luid(workbook_luid):
    """
    Retrieves a PDF for a view by its LUID.
    """

    server, tableau_auth = get_tableau_server_and_auth()
    view_pdfs = []

    with server.auth.sign_in(tableau_auth):
        tsc_wb = server.workbooks.get_by_id(workbook_luid)

        server.workbooks.populate_views(tsc_wb)

        for view in tsc_wb.views:
            pdf_req_option = TSC.PDFRequestOptions()
            pdf_req_option.page_type = TSC.PDFRequestOptions.PageType.Letter
            pdf_req_option.orientation = TSC.PDFRequestOptions.Orientation.Landscape

            server.views.populate_pdf(view, pdf_req_option)
            view_pdfs.append({"name": view.name, "pdf": view.pdf})

        return view_pdfs
