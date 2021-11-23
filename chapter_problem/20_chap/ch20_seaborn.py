import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips)

plt.show()

# raise URLError(err)
# urllib.error.URLError: < urlopen error[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate(_ssl.c: 1123) >
