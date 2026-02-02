import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

def plot_metric(df, scenario, metric, outfile):  
    plt.figure()
    single=df[(df['scenario']==scenario)&(df["mode"]=="single")].sort_values("k")
    multi=df[(df['scenario']==scenario)&(df["mode"]=="multi")].sort_values("k")

    plt.plot(single["k"],single[metric],label=f'{scenario}_single')
    plt.plot(multi["k"],multi[metric],label=f'{scenario}_multi')

    plt.title(f'{scenario.capitalize()}: k vs {metric}')
    plt.xlabel('window size (k)')
    plt.ylabel(metric)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile,dpi=300)
    plt.close()
plot_metric(df, "recon", "mismatch_rate","plots/recon_mismatch.png")
plot_metric(df, "recon", "coverage","plots/recon_coverage.png")
plot_metric(df, "priv", "mismatch_rate","plots/priv_mismatch.png")
plot_metric(df, "priv", "coverage","plots/priv_coverage.png")
