from WriteEquations import ParseReactions
from WriteEquationsNetwork2 import NetworkToReactions
Network = [
("Wnt", "Fzl", 3, "none"),
("Wnt_Fzl", "Dvl", 1, "none"),
("Wnt_Fzl", "MMPs", 1, "none"),
("MMPs", "TGFa", 1, "none"),
("TGFa", "NKD2", 1, "none"),
("NKD2", "Dvl", 2, "none"),
("Axin", "APC", 3, "none"),
("Axin_APC", "GSK3B", 4, "none"),
("GSK3B_Axin_APC", "GSK3B_Axin_APC", 8, "none"),
("GSK3B_Axin_APC", "Bcat", 4, "none"),
("GSK3B_Axin_APC_Bcat", "GSK3B_Axin_APC_Bcat", 8, "none"),
("GSK3B_Axin_APC_Bcat", "Bcat", 9, "none"),
("GSK3B_Axin_APC", "Dvl", 7, "GSK3B"),
("IGF", "IGFR", 1, "none"),
("IGFR", "IRS1", 1, "none"),
("IRS1", "PI3K", 1, "none"),
("PI3K", "PIP3", 1, "none"),
("PIP3", "PDK1", 1, "none"),
("PDK1", "Akt", 1, "none"),
("Akt", "TSC2", 2, "none"),
("TSC2", "Rheb", 2, "none"),
("Rheb", "Mtor", 1, "none"),
("Mtor", "P7056K", 1, "none"),
("P7056K", "IRS1", 2, "none"),
("PTEN", "PIP3", 2, "none"),
("Phlpp", "Akt", 2, "none"),
("LKB1", "AMPK", 1, "none"),
("Akt", "AMPK", 2, "none"),
("AMPK", "TSC2", 1, "none"),
("AMPK", "Mtor", 2, "none"),
("PDK1", "PKC", 1, "none"),
("PDK1", "RSK2", 1, "none"),
("EGF", "EGFR", 1, "none"),
("EGFR", "Grb2", 3, "none"),
("EGFR_Grb2", "Gab1", 4, "none"),
("EGFR_Grb2_Gab1","EGFR_Grb2_Gab1", 8, "none"),
("EGFR", "Shc", 4, "none"),
("EGFR_Shc", "EGFR_Shc", 8, "none"),
("EGFR_Shc", "Grb2", 3, "none"),
("EGFR", "Msos", 1, "none"),
("EGFR_Shc_Grb2", "Msos", 3, "none"),
("EGFR_Shc_Grb2_Msos", "Ras", 1, "none"),
("Ras", "Raf", 1, "none"),
("Raf", "Mek", 1, "none"),
("Mek", "Erk", 1, "none"),
("Mek", "P38MAPK", 1, "none"),
("Erk", "P90RSK", 1, "none"),
("NGF", "NGFR", 1, "none"),
("NGFR", "C3G", 1, "none"),
("C3G", "Rap1", 1, "none"),
("Rap1", "BRaf", 1, "none"),
("ATM", "MDM2", 2, "none"),
("MDM2", "P53", 2, "none"),
("Rb", "MDM2", 2, "none"),
("P53", "P21", 1, "none"),
("P21", "Ecdk2", 2, "none"),
("Ecdk2", "Rb", 2, "none"),
("Ecdk2", "MDM2", 2, "none"),
("ATM", "P53", 1, "none"),
("P53", "SIAH1", 1, "none"),
("P1914ARF", "MDM2", 2, "none"),
("P53", "WIP1", 1, "none"),
("WIP1", "P38MAPK", 2, "none"),
("TGFa", "EGFR", 1, "none"),
("Bcat", "EGFR", 1, "none"),
("SIAH1", "Bcat", 2, "none"),
("Bcat", "P1914ARF", 1, "none"),
("GSK3B", "TSC2", 1, "none"),
("Akt", "GSK3B", 2, "none"),
("GSK3B", "P53", 3, "none"),
("IGFR", "Shc", 1, "none"),
("IRS1", "Grb2", 1, "none"),
("EGFR_Grb2_Gab1", "PI3K", 1, "none"),
("PKC", "Raf", 1, "none"),
("RSK2", "EGFR_Grb2_Gab1", 2, "none"),
("P90RSK", "IRS1", 2, "none"),
("P53", "PTEN", 1, "none"),
("Akt", "MDM2", 1, "none"),
("Akt", "Raf", 2, "none"),
("IRS1", "Mek", 1, "none"),
("NGFR", "Msos", 1, "none"),
("BRaf", "Mek", 1, "none"),
("PP2A", "Ras", 2, "none"),
("PP2A", "Raf", 2, "none"),
("PP2A", "GSK3B_Axin_APC", 2, "none"),
("PP2A", "CdkG", 3, "none"),
("CdkG_PP2A", "MDM2", 1, "none"),
("P38MAPK", "P53", 1, "none")
]
reactions = NetworkToReactions(Network)
equations = ParseReactions(reactions)
print(equations)
