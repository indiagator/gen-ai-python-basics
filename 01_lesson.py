import numpy as numpy

print("we are learning python!")

temperature  = 18.0
threshold = 24

if  temperature > threshold:
    print("it is hot today")
else:
    print("it is cool today")

# first demo over

ai_accuracy = 34

if ai_accuracy >= 90:
    print("🔥 Amazing model! Ready to deploy!")
elif ai_accuracy >= 70:
    print("👍 Pretty good, but needs more training data.")
elif ai_accuracy >= 50:
    print("😐 Meh. Keep improving.")
else:
    print("💀 This model needs a lot of work...")


# second demo over

spam_probability = 0.95

if spam_probability > 0.8:
    print("📧 Move to SPAM folder")
else:
    print("📬 Deliver to inbox")