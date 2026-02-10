def serve_chai(flavor):
    try:
        print(F"Preparing {flavor} chai....")
        if flavor == "unknown":
            raise ValueError("We do not have that flavor of chai")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is ready to be served!")
    finally:
        print("Next customer please")

serve_chai("masala") # Valid flavor
serve_chai("unknown") # Invalid flavor