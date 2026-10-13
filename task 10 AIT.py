# Student facts
student = {
    "age": 20,
    "dept": "Computer Science",
    "city": "Chennai",
    "python": True,
}

# Verification
is_verified = (
    student["age"] == 20
    and student["dept"] == "Computer Science"
    and student["city"] == "Chennai"
    and student["python"] is True
)

# Output
print(
    "All facts verified successfully!"
    if is_verified
    else "Verification failed."
)
