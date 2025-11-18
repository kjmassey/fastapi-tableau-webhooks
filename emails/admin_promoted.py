ADMIN_PROMOTED_EMAIL_BODY_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tableau Alert (via Webhooks)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0; padding:0; background-color:#f3f4f6;">
  <!-- Full-width wrapper -->
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color:#f3f4f6; padding:20px 0;">
    <tr>
      <td align="center">
        <!-- Main container -->
        <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="background-color:#ffffff; border-radius:6px; overflow:hidden; font-family:Arial, sans-serif;">
          
          <!-- Header / Logo -->
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
                We wanted to let you know that a new user has been promoted to an Admin Role on your site:
              </p>

              <p style="margin:0 0 6px 0;">
                <strong>Site name:</strong><br><br>
                [[SITE_NAME]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 6px 0;">
                <strong>User name:</strong><br><br>
                [[USER_NAME]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 6px 0;">
                <strong>User's new site role:</strong><br><br>
                [[USER_ROLE]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 16px 0;">
                <strong>Event Date:</strong><br><br>
                [[EVENT_DATE]]<br>
                __________________________________
              </p>

              <p style="margin:0 0 8px 0;">
                If this was intentional, you can safely ignore this alert. If not, you'll want to demote this user and research ASAP!
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
