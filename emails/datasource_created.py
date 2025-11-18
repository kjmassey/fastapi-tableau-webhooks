DATASOURCE_CREATED_EMAIL_BODY_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>New Datasource Published</title>
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
                Hello Data Explorers,
              </p>

              <p style="margin:0 0 16px 0;">
                Great news — a <strong>new datasource</strong> has just been published to your Tableau site! Fresh data means fresh insights, and this is your chance to dig in and uncover what’s new.
              </p>

              <p style="margin:0 0 6px 0;">
                <strong>Site name:</strong><br><br>
                [[SITE_NAME]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 6px 0;">
                <strong>Datasource name:</strong><br><br>
                [[DATASOURCE_NAME]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 6px 0;">
                <strong>Published by:</strong><br><br>
                [[PUBLISHED_BY]]<br>
                __________________________________
              </p>
              <p style="margin:0 0 16px 0;">
                <strong>Link:</strong><br><br>
                [[LINK]]<br>
              </p>

              <p style="margin:0 0 16px 0;">
                New data is a perfect opportunity to refresh dashboards, validate assumptions, or explore emerging trends. Head over to your Tableau site and start exploring to see what insights you can uncover!
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
