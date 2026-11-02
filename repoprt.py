#Day one of returning, Short in Dictionries

def main():
    spacecraft ={"name": "James Webb Space Telescope"}
    spacecraft.update({"Distance": 0.01, "Orbit": "Sun"})
    print(Creat_report(spacecraft))

def Creat_report(spacecraft):
    return f"""
    ====== Report =======

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("Distance", "Unknown ")} AU
    Orbit: {spacecraft.get ("Orbit", "Unknown")}
    =====================
    """
main()