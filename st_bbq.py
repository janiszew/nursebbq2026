import streamlit as st

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def format_yn(answer):
  mapping = {"yes": "Yes, with exuberance in my heart", "no": "No, and the regret gnaws at me like a rat"}
  return mapping.get(answer)

st.title("Otago Nursing Masters End of Year BBQ 2026!")

st.write("WHERE: North Hagley Park, south of Victoria Lake between the Armagh parking lot and the tennis courts")

st.image("bbq1.png")

st.write("WHEN: Saturday 21st November, noon till we're done")
st.write("WHAT: A bbq, meat and veg options, gluten free stuff as well")
st.write("WHO: You! Your family! Your friends!")

st.write("\n\nWhat to bring: seating, blankets, shade, and then a plate to share or drinks if you're interested, but no pressure!")

with st.form("email"):
  sender = "twah.nz.441@gmail.com"
  sender_password = "vnldlgpemvhmfmli "

  receiver_name = st.text_input("name:")
  receiver_email = "janiszew@gmail.com"

  subject = "rsvp from " + receiver_name

  attendance = st.radio("Are you coming on 21st November, noon until they throw us out, to North Hagley Park?",
                        ["yes",
                         "no"],
                        format_func=format_yn)

  attendees = st.selectbox("I am bringing this many hungry people:",
                           ["1",
                            "2",
                            "3",
                            "4",
                            "5+"])

  st.write("Anything you'd like us to know, dietary restrictions etc?")

  receiver_notes = st.text_input("notes for the planners:")

  submit_button = st.form_submit_button("Send Email")

if submit_button:
  if not receiver_email or not receiver_name:
    st.error("Please add your email and name")
  else:
    body = f"{receiver_name}:\n\n"
    if attendance == "yes":
      body += "bringing " + attendees + " people\n\n"
      body += "dietary notes: " + receiver_notes
    else:
      body = "not coming!"

    try:
      msg = MIMEMultipart()
      msg['From'] = sender
      msg['To'] = receiver_email + ", twah.nz.441@gmail.com"
      msg['Subject'] = subject
            
      msg.attach(MIMEText(body, 'plain'))
            
      with smtplib.SMTP('smtp.gmail.com', 587) as server:
          server.starttls()  # Secure the connection
          server.login(sender, sender_password)
          server.sendmail(sender, receiver_email, msg.as_string())
                
      st.success("Email sent successfully!")

    except Exception as e:
      st.error(f"Failed to send email. Error: {e}")
