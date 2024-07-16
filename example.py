from monetize import monetize
from flask import *

######
# Basic Example

# Taken from Stripe
stripe_key = 'sk_live_abcdef123'

# Initialize
m = monetize(stripe_key)

# Returns true or false which means it charged the subscription
if m.accrue(1,'si_abcdef123'):
    print('Customer charged')
else:
    print('Customer not charged')
    
###### 

######  
# FLASK example where API key from a customer may be linked to a subscription
app = Flask(__name__)

@app.route('/api/stuff', methods=['GET'])
def stuff():
    
    # 1. Validate credentials and charge user
    user_validated = False # user validation
    user = {
        "user_id":"",
        "sid":""
            } # user object, sid is the subscription item id linked to the user
    
    
    # we'll say a command was run in this condition to validate the user
    if user_validated == True:
        # After user is validated
        m = monetize(stripe_key)
        m.accrue(1,user['sid']) # Charge the user's sid for the API use
    else:
        return "Unauthorized"
        
    # 2. Continue with regular API usage
    if request.method == "GET":
        return "We charged you"

###### 