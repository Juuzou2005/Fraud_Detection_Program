import matplotlib.pyplot as Plot
import numpy




class DataComparing:
    def __init__(self, data):
        self.data =numpy.array(data)

    def RepFraudNormal(self): #reprezentasion of Fraud and Normal tranzactions
        labels = numpy.array(self.data[:, -1])
        count_Normal = numpy.sum(labels == 0)
        count_Fraud = numpy.sum(labels == 1)

        Plot.bar(["Normal tranz", "Fraud tranz"],[count_Normal, count_Fraud], color=["green", "red"])
        Plot.xlabel("Transaction Type")
        Plot.ylabel("Count")
        Plot.title(f"Fraud({count_Fraud})({round(count_Fraud*100/(count_Normal+count_Fraud), 2)}%) "
                   f"vs Normal({count_Normal})({round(count_Normal*100/(count_Normal+count_Fraud), 2)}%)")
        Plot.show()

    def BoxPLot(self):
        labels = self.data[:, -1]
        amounts = self.data[:, -2]
        print(numpy.mean(amounts))
        normal_amounts = amounts[labels == 0]
        fraud_amounts = amounts[labels == 1]
        Plot.boxplot([normal_amounts, fraud_amounts], labels=["Normal tranz", "Fraud tranz"])
        Plot.xlabel("Transaction Type")
        Plot.ylabel("Amount")
        Plot.title("Distribuția sumelor (Boxplot) - Zoom până la 500$")
        Plot.show()


    def ScaterPlot(self):
        time = self.data[:, 0]
        amounts = self.data[:, -2]
        labels = self.data[:, -1]

        # Separăm tranzacțiile normale de cele frauduloase
        time_normal = time[labels == 0]
        amount_normal = amounts[labels == 0]

        time_fraud = time[labels == 1]
        amount_fraud = amounts[labels == 1]

        Plot.figure(figsize=(10, 6))

        # TRUC DE PRO: Desenăm tranzacțiile normale primele, cu verde și foarte transparente (alpha=0.1)
        # Dacă nu punem transparență, cele 284.000 de puncte verzi vor acoperi tot ecranul
        Plot.scatter(time_normal, amount_normal, color='green', alpha=0.1, label="Normal tranz", marker='o')

        # Desenăm fraudele cu roșu, netransparente, ca să iasă în evidență peste stratul verde
        Plot.scatter(time_fraud, amount_fraud, color='red', alpha=1.0, label="Fraud tranz", marker='x')

        Plot.xlabel("Timpul scurs de la prima tranzacție (secunde)")
        Plot.ylabel("Suma (Amount)")
        Plot.title("Corelația Timp vs. Sumă (Scatter Plot)")
        Plot.legend()

        Plot.show()

