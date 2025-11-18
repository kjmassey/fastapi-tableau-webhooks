WORKBOOK_REFRESH_FAILED_EMAIL_BODY_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Workbook Refresh Failed</title>
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
                Hello Admins,
              </p>

              <p style="margin:0 0 16px 0;">
                A scheduled <strong>workbook refresh has failed</strong> on your Tableau site. When refreshes stop running successfully, dashboards can quickly become outdated — potentially impacting business decisions and downstream reporting.
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
                <strong>Failure time:</strong><br><br>
                [[FAILURE_TIME]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 16px 0;">
                <strong>Owner:</strong><br><br>
                [[OWNER]]<br>
                __________________________________
              </p>              
              <p style="margin:0 0 16px 0;">
                <strong>Link:</strong><br><br>
                [[LINK]]<br>
                __________________________________
              </p>

              <p style="margin:0 0 16px 0;">
                Please review the datasource connection details, credentials, and any upstream system availability as soon as possible. Resolving the issue helps ensure your dashboards remain accurate, timely, and ready for your users.
              </p>

              <p style="margin:0;">
                Thanks,<br>
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
