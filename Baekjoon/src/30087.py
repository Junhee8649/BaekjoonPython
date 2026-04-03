N = int(input())
seminas = {
    "Algorithm":  204,
    "DataAnalysis": 207,
    "ArtificialIntelligence": 302,
    "CyberSecurity": "B101",
    "Network": 303,
    "Startup": 501,
    "TestStrategy": 105
}
for _ in range(N):
    semina = input()
    print(seminas[semina])