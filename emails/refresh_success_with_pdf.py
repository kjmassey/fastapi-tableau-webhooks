REFRESH_SUCCESS_WITH_PDF_EMAIL_BODY_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Your PDF Is Attached</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0; padding:0; background-color:#f3f4f6;">
  <!-- Full-width wrapper -->
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color:#f3f4f6; padding:20px 0;">
    <tr>
      <td align="center">
        <!-- Main container -->
        <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="background-color:#ffffff; border-radius:6px; overflow:hidden; font-family:Arial, sans-serif;">
          
          <!-- Header -->
          <tr>
            <td align="center" style="background-color:#1f4f82; padding:16px 24px;">
              <span style="font-size:20px; font-weight:bold; color:#ffffff; text-align:center; display:block;">
                Tableau Alert (via Webhooks)
              </span>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding:24px 24px 28px 24px; color:#111827; font-size:14px; line-height:1.6;">
              
              <p style="margin:0 0 16px 0;">
                Hello,
              </p>

              <p style="margin:0 0 16px 0;">
                Good news — your scheduled refresh has completed successfully, and your <strong>latest PDF export is now attached</strong>. This means fresh data is ready for you to review and share.
              </p>

              <p style="margin:0 0 6px 0;">
                <strong>Site name:</strong><br><br>
                [[SITE_NAME]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 6px 0;">
                <strong>Workbook name:</strong><br><br>
                [[WORKBOOK_NAME]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 16px 0;">
                <strong>Owner:</strong><br><br>
                [[OWNER]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 16px 0;">
                <strong>Completed at:</strong><br><br>
                [[COMPLETED_AT]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 16px 0;">
                <strong>Link:</strong><br><br>
                [[LINK]]<br>
                __________________________________
              </p>


              <p style="margin:0 0 16px 0;">
                With updated data now available, you can explore trends, monitor KPIs, and share the latest insights with your team. If you rely on this report regularly, rest easy—your most current snapshot is ready to go.
              </p>

              <p style="margin:0;">
                Happy analyzing,<br>
                Your Tableau Team
              </p>

            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""
