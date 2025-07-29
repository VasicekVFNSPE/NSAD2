import uproot
import numpy as np
import matplotlib.pyplot as plt
import os

pt_sources = {
        "ISR:on, FSR:on": ("srazka_higgs_on_on.root", "pT_on_on"),
        "ISR: on, FSR:off": ("srazka_higgs_on_off.root", "pT_on_off"),
        "ISR: off, FSR:on": ("srazka_higgs_off_on.root","pT_off_on"), 
        "ISR: off, FSR:off": ("srazka_higgs_off_off.root","pT_off_off")

}

# vzor pojmenovani histogramu: pT_on_on, y_on_on


styles = {
	"ISR:on, FSR:on": ("black", "-"),
        "ISR: on, FSR:off": ("red", "--"),
        "ISR: off, FSR:on": ("blue", ":"),
        "ISR: off, FSR:off": ("green", "-.")
}

def load_hist(file_path, hist_name):
    with uproot.open(file_path) as f:
        hist = f[hist_name]
        values = hist.values()
        edges = hist.axes[0].edges()
        centers = 0.5 * (edges[1:] + edges[:1])
        norm_values = values / np.sum(values) if np.sum(values) > 0 else values
    return norm_values, centers
#nahrani dat histogramu z root souboru


def plot_overlay(sources, xlabel, title, output_filename):
    plt.figure(figsize=(10, 6))
    for label, (filename, histname) in sources.items():
        values, centers = load_hist(filename, histname)
        color, linestyle = styles[label]
        plt.step(centers, values, where="mid", label=label, color=color, linestyle=linestyle)
    plt.xlabel(xlabel)
    plt.ylabel("Normalized events")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    	#plt.savefig(output_filename, dpi=300)
    	#plt.close()
    	#print(f"Uložen obrázek: {output_filename}")

plot_overlay(pt_sources, r"Transverse momentum $p_T$ [GeV]", "Pricna hybnost - vsechna nastaveni", "prolozeni_pt.png")
