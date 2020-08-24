class Email:

	def get_email(self, items):
		email_string = """
			<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
			<html xmlns="http://www.w3.org/1999/xhtml">
			<head>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
			<title>Price Tracker Email</title>
			<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
			</head>
			<body style="margin:0;padding:0;background-color:#f6f6f6">
			    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="padding-top:20px;"> 
			        <tr>
			            <td>
			                <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse:collapse;">
			                    <tr>
			                        <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;border-radius:20px;">
			                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
			                                <tr>
			                                    <td style="font-family: sans-serif; font-size: 24px;">
			                                        <h1 style="color:#000000;font-family:sans-serif;font-size:35px;font-weight:300;text-align:center;">Your Price Tracker Updates</h1>
			                                    </td>
			                                </tr>
			                                <tr>
			                                    <td>
			                                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
			                                        	""" + self.items_to_strings(items) + """
			                                            <tr>
			                                              <td style="padding: 20px 0px;">
			                                                <a href="http://localhost:3000/" target="_blank" style="font-family:sans-serif;cursor:pointer;border-radius:5px;font-size:14px;font-weight:bold;margin:0;padding:12px 25px;text-decoration:none;background-color:black;border:none;color:#ffffff;display:block;width:70px;text-align:center;">Visit Items</a>
			                                              </td>
			                                           </tr>
			                                        </table>
			                                    </td>
			                                </tr>
			                            </table>
			                        </td>
			                    </tr>
			                </table>
			                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin-top:20px;margin-bottom:20px;">
			                  <tr>
			                    <td style="font-family:sans-serif;color:#999999;font-size:12px;text-align:center;">
			                        By <a href="https://ivanmtta.github.io/" style="color:#999999;text-decoration:none;">Ivan Mota</a>
			                    </td>
			                  </tr>
			                </table>
			            </td>
			        </tr>
			    </table>
			</body>
			</html>
		"""
		return email_string

	def items_to_strings(self, items):
		result_string = ""
		for item in items:
			result_string += """
				<tr>
					<td width="260" valign="top">
						<table border="0" cellpadding="0" cellspacing="0" width="100%">
							<tr>
								<td>
									<img src='""" + item["image"] + """' alt="" width="100%" height="180" style="display:block;" />
								</td>
							</tr>
						</table>
					</td>
					<td style="font-size:0;line-height:0;" width="20">
						&nbsp;
					</td>
					<td width="260" valign="top">
						<table border="0" cellpadding="0" cellspacing="0" width="100%">
							<tr>
								<td style="font-family:sans-serif;font-size:16px;line-height:20px;">
									""" + item["name"] + """
								</td>
							</tr>
							<tr>
								<td>&nbsp;</td>
							</tr>
							<tr>
								<td style="font-family:sans-serif;font-size:14px;line-height:20px;">
									<b>Original Price: $""" + str(item["original_price"]) + """</b>
								</td>
							</tr>
							<tr>
								<td style="font-family:sans-serif;font-size:14px;line-height: 20px;">
									<b>Current Price: $""" + str(item["current_price"]) + """</b>
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr style="height:40px;">
					<td>&nbsp;</td>
				</tr>
			"""
		return result_string
