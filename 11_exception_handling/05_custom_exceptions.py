def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError(f"Unsupported chai flavor: {flavor}")
    
brew_chai("mint")