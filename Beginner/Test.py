def daniel_actions(name = "Daniel", action = "sleeping", how = "noisy"):
    print(name, action, how)

daniel = ["Petur", "having", "fun"]
Vasia = ["Vasia", "playing", "cards"]


daniel_actions(*daniel)
daniel_actions(*Vasia)

daniel_actions(action = "working")