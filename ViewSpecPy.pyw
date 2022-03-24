# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)
# and Josicleda Galvincio (josicleda@gmail.com)

import io, sys, math
import tkinter.messagebox as tkMessageBox
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfile 

class ViewSpecPy(object):
    def __init__(self):
        self.header = ''    # this initializes self.header
        self.dict = {}
        self.indices = {}

    def add(self, t):
        t = t.split(',')
        key = int(float(t[0]))  # this is to handle the invalid literal for int()
        value = float(t[1])
        self.dict[key] = value

    def load(self, reader, i):
        for j in range(len(reader)):   # this iterates through the lines
            # this splits the row
            row = reader[j].split('\t')[1:]
            # this defines the header
            if j == 0:
                self.header = row = row[i]  # Populates self.header
                continue
            # this adds the
            # data to the 
            # dict object
            self.add(row[i])    # this populates self.dict
    
    def derivative(self, gap):
        # this calculates the
        # 1st derivative
        i = self.dict.keys()    # this gets the wavelengths
        j = list(map(float, self.dict.values()))  # this gets the values and converts them into float
        m = gap/2   # this gets the median of the gap
        r = []
        for l in range(len(self.dict)):
            if (l+1 <= m) or (l+1 >= (len(self.dict) - m)):
                # this fills the values before
                # (at the begining)
                # and after (at the end)
                # the median of the gap
                # as 0 (zero)
                r.append(0)
            else:
                # this calculates
                # the 1st
                # derivative data
                x = (j[l-m] - j[l+m]) / (i[l-m] - i[l+m])
                x = round(x, 3) # this rounds the value to a 3 decimal number
                r.append(x)
        return r

    def process(self):
        # this creates an string-array
        # of bands
        def interval(mn, mx):
            v = []
            for i in range(mn, mx+1):
                v.append("i[" + str(i) + "]")
            v = ", ".join(v)
            return(v)

        i = self.dict
        j = self.indices
        # l = self.derivative(7)

        mn = min(i.keys())
        mx = max(i.keys())

        o = []

        # this populates self.indices
        # To add new indices here
        # you must edit the following
        # lines
        if mx > 1075:
            o = o + ["j['NDWI'] = (i[860] - i[1240]) / (i[860] + i[1240])"]

        o = o + ["j['PRI1'] = (i[531] - i[570]) / (i[531] + i[570])",
        # "j['SPRI1'] = (j['PRI1']  + 1) / 2",
        # "j['SPRI2'] = (j['PRI2']  + 1) / 2",
        # "j['SR705'] = i[750] / i[705]",
        # "j['R(red_edge)'] = (i[670] + i[780]) / 2",
        # "j['NPP1_umol_m-2_s-1'] = - (-5.6*(j['NDVI'] * j['SPRI1']) - 0.69)",
        # "j['NPP2_umol_m-2_s-1'] = - (-5.6*(j['NDVI'] * j['SPRI2']) - 0.69)",
        # "j['CO2_1_umol_m-2_s-1'] = - (-4.3833 - 15.018 * (j['SPRI1'] * j['NDVI']))",
        # "j['CO2_2_umol_m-2_s-1'] = - (-4.3833 - 15.018 * (j['SPRI2'] * j['NDVI']))",
        # "j['WI'] = i[900] / i[970]",
        # "j['LAI_Galvincio'] = math.exp(1.426 + (-0.542 / j['NDVI']))",
        # "j['GPP_umol_m-2_s-1'] = (j['WDVI'] + 0.2782) / 0.2137"]
        # "j['ChlNDI'] = (i[750] - i[705]) / (i[750] + i[705])",
        # "j['Ant_Gitelson'] = ((1 / i[550]) - (1 / i[700])) * i[780]",
        "j['ARVI'] = ((i[800] - 2) * (i[800] - i[450])) / ((i[800] + 2) * (i[800] - i[450]))",
        "j['BGI'] = i[400] / i[550]",
        "j['BNDVI'] = (i[800] - i[450]) / (i[800] + i[450])",
        "j['Boochs_1'] = i[703]",
        "j['Boochs_2'] = i[720]",
        "j['BGBO'] = (i[495] / i[554]) / (i[495] / i[635])",    
        "j['BRI'] = i[400] / i[690]",
        "j['CAI_1'] = 0.5 * (i[2000] + i[2200]) - i[2100])",
        "j['CAI_2'] = 0.5 * (i[2031] + i[2211]) - i[2101])", 
        "j['Carter_1'] = i[695] / i[420]",
        "j['Carter_2'] = i[695] / i[760]",
        "j['Carter_3'] = i[605] / i[760]",
        "j['Carter_4'] = i[710] / i[760]",
        "j['Carter_5'] = i[695] / i[670]",
        "j['Carter_6'] = i[550]",
        "j['CI_1'] = (i[750] - i[705]) / (i[750] + i[705])",
        "j['CI_2'] = (i[760] / i[700]) - 1",
        "j['CI_green'] = (i[800] / i[550]) - 1",
        "j['CI_red_edge'] = (i[750] / i[710]) - 1",
        "j['CTR_1'] = i[695] / i[420]",
        "j['CTR_2'] = i[695] / i[760]",
        "j['CUR'] = (i[675] * i[690]) / i[683]**0.5",
        "j['CRI_1'] = (1 / i[510]) - (1 / i[550])",
        "j['CRI_2'] = (1 / i[510]) - (1 / i[770])",
        "j['CRI_3'] = (1 / i[515]) - (1 / i[550])",
        "j['CRI_4'] = (1 / i[515]) - (1 / i[770])",
        "j['CRI_5'] = (1 / i[515]) - (1 / i[550]) * i[770]",
        "j['CRI_6'] = (1 / i[515]) - (1 / i[770]) * i[770]",
        "j['DATT'] = i[672] / (i[708] * i[550])",
        "j['Datt_1'] = (i[850] - i[710]) / (i[850] + i[680])",
        "j['Datt_2'] = (i[850] / i[710])",
        "j['Datt_3'] = (i[754] / i[704])",
        "j['Datt_5'] = (i[672] / i[550])",
        "j['Datt_7'] = (i[860] - i[2218]) / (i[860] - i[1928])",
        "j['Datt_8'] = (i[860] - i[1788]) / (i[860] - i[1928])",
        "j['DD'] = (i[749] - i[720]) - (i[701] - i[672])",
        "j['D1'] = i[730] / i[706]",
        "j['D2'] = i[705] / i[722]",
        "j['DMCI_D'] = (i[2305] - i[1550]) / (i[2305] + i[1550])",
        "j['DSI'] = (i[1648] - i[498]) / (i[1648] - i[2203] + 0.2)",
        "j['DVI'] = (i[810] / i[680])",
        "j['DWSI_1'] = (i[800] / i[1660])",
        "j['DWSI_2'] = (i[1660] / i[550])",
        "j['DWSI_3'] = (i[1660] / i[680])",
        "j['DWSI_4'] = (i[550] / i[680])",
        "j['DWSI_5'] = (i[800] + i[550]) / (i[1660] + i[680])",
        "j['EGFN'] = (max(i[650], i[750]) - max(i[500], i[550]))/(max(i[650], i[750]) + max(i[500], i[550]))",
        "j['ExG'] = 2 * (mean(interval(520,560)) - mean(interval(630,690)) - mean(interval(430,470)))",
        "j['EVI_1'] = 2.5 * ((i[782] - i[675]) / (i[782] + (6 * i[675]) - (7.5 * i[445]) + 1)",
        "j['EVI_2'] = 2.5 * ((i[800] - i[660]) / (i[800] + (2.4 * i[660]) + 1))",
        "j['FRI_1'] = i[690] / i[600]",
        "j['FRI_2'] = i[740] / i[800]",
        "j['GARI'] = (i[800] / i[530]) - 1",
        "j['GCI'] = (i[800] + i[550]) - 1",
        "j['GI'] = i[544] / i[677]",
        "j['GIT'] = ((i[750] - i[800]) / (i[695] - i[740])) - 1",
        "j['Gitelson_1'] = 1 / (i[700])",
        "j['GM_1'] = i[750] / i[550]",
        "j['GM_2'] = i[750] / i[700]",
        "j['GNDVI_1'] = (i[750] - i[540] + i[570]) / (i[750] + i[540] - i[570])",
        "j['GNDVI_2'] = (i[780] - i[550]) / (i[780] + i[550])",
        "j['GNDVI_3'] = (i[800] - i[550]) / (i[800] + i[550])",
        "j['GNDVI_4'] = (i[750] - i[550]) / (i[750] + i[550])",
        "j['GVMI'] = ((i[820] + 0.1)-(i[1600] + 0.02)) / ((i[820] + 0.1)+(i[1600] + 0.02))",
        "j['LCA'] = 2 * i[2205] - (i[2165] + i[2330])",
        "j['LIC'] = i[440] / i[740]",
        "j['Infrared_to_green_ratio'] = i[780] / i[550]",
        "j['Infrared_to_red_ratio'] = i[780] / i[670]",
        "j['LWI'] = i[1300] / i[1450]",
        "j['LWVI_1'] = (i[1094] - i[983]) / (i[1094] + i[983])",
        "j['LWVI_2'] = (i[1094] - i[1205]) / (i[1094] + i[1205])",
        "j['Maccioni'] = (i[780] - i[710]) / (i[780] - i[680])",
        "j['mARI'] = 800 * ((1 / i[550]) - (1 / i[700])",
        "j['MCARI_1'] = ((i[700] - i[670]) - 0.2 * (i[700] - i[550])) * (i[700] / i[670])",
        "j['MCARI_2'] = (i[750] - i[705]) - 0.2 * (i[700] - i[550]) * (i[750] - i[705])",
        "j['MDMI_2'] = (860 - (i[1640] - i[2130])) / (860 + (i[1640] - i[2130]))",
        "j['mNDVI_1'] = (i[800] - i[680]) / (i[800] + i[680] - 2 * i[445])",
        "j['mNDVI_2'] = (i[750] - i[673]) / (i[800] + i[673] - 2 * i[445])",
        "j['mND705'] = (i[750] - i[750]) / (i[750] + i[705] - 2 * i[445])",
        "j['MPRI'] = (i[515] - i[530]) / (i[515] + i[530])",
        "j['mRESR'] = (i[750] - i[445]) / (i[705] + i[445])",
        "j['MSAVI'] = 0.5 * (2 * i[800] + 1 - ((2 * i[800]) + 1**0.5 - 8 * (i[800] - i[670]))",
        "j['MSI_1'] = i[1650] / i[830]",
        "j['MSI_2'] = i[1600] / i[820]",
        "j['MSI_3'] = i[1600] / i[817]",
        "j['mSR705'] = (i[750] - i[445]) / (i[750] - i[445])",
        "j['MTVI'] = 1.2 * (1.2 * (i[800] - i[550]) - 2.5 * (i[670] - i[550])",
        "j['NAI'] = (i[780] - i[570]) / (i[780] - i[570])",
        "j['ND'] = (i[800] - i[700]) / (i[800] + i[700])",
        "j['NDDAig'] = (i[755] + i[680] - 2 * i[705]) / (i[755] - i[680])",
        "j['NDII'] = (i[860] - i[1600]) / (i[860] + i[1600])",
        "j['NDLI'] = (math.log(1 / i[1754]) - math.log(1 / i[1680]))/ (math.log(1 / i[1754]) + math.log(1 / i[1680]))",
        "j['NDMI_1'] = (i[2200] - i[1100]) / (i[2200] + i[1100])",
        "j['NDMI_D'] = (i[1742] - i[1660]) / (i[1742] + i[1660])",
        "j['NDNI'] = (math.log(1 / i[1510]) - math.log(1 / i[1680]))/ (math.log(1 / i[1510]) + math.log(1 / i[1680]))",
        "j['NDRE'] = (i[800] - i[720]) / (i[800] + i[720])",
        "j['NDVI_1'] = (i[800] - i[670]) / (i[800] + i[670])",
        "j['NDVI_2'] = (i[900] - i[680]) / (i[900] + i[680])",
        "j['NDVI_3'] = (i[800] - i[680]) / (i[800] + i[680])",
        "j['NDVI_4'] = (i[682] - i[553]) / (i[682] + i[553])",
        "j['NDVI_5'] = (i[895] - i[675]) / (i[895] + i[675])",
        "j['NDVI_6'] = (i[750] - i[650]) / (i[750] + i[650])",
        "j['NDVI_7'] = (i[750] - i[673]) / (i[750] + i[673])",
        "j['NDVI_8'] = (i[750] - i[675]) / (i[750] + i[675])",
        "j['NDVI_9'] = (i[750] - i[680]) / (i[750] + i[680])",
        "j['NDWI_1'] = (i[860] - i[1240]) / (i[860] + i[1240])",
        "j['NDWI_2'] = (i[857] - i[1241]) / (i[857] + i[1241])",
        "j['NDWI_D'] = (i[860] - i[2270]) / (i[860] + i[2270])",
        "j['NGBDI'] = (mean(interval(520,560)) - mean(interval(430,470))) / (mean(interval(520,560)) + mean(interval(430,470)))",
        "j['NPCI'] = (i[680] - i[430]) / (i[680] + i[430])",
        "j['NPQI'] = (i[415] - i[435]) / (i[415] + i[435])",
        "j['NRI'] = (i[570] - i[670]) / (i[570] + i[670])",
        "j['NTCI'] = (i[754] - i[709]) / (i[709] - i[681])",
        "j['NVI'] = (i[777] - i[747]) / i[673]",
        "j['NWI_1'] = (i[970] - i[900]) / (i[970] + i[900])",
        "j['NWI_2'] = (i[970] - i[850]) / (i[970] + i[850])",
        "j['NWI_3'] = (i[970] - i[880]) / (i[970] + i[880])",
        "j['NWI_4'] = (i[970] - i[920]) / (i[970] + i[920])",
        "j['OSAVI'] = ((1 + 0.16) * (i[800] - i[670])) / (i[800] + i[670] + 0.16)",
        "j['PARS'] = i[746] / i[513]",
        "j['PI_1'] = (i[522] - i[504]) / (i[522] + i[504])",
        "j['PI_2'] = (i[551] - i[562]) / (i[551] + i[562])",
        "j['PI_3'] = (i[700] - i[680]) / (i[700] + i[680])",
        "j['PI_4'] = (i[782] - i[700]) / (i[782] + i[700])",
        "j['PI_5'] = (i[782] - i[671]) / (i[782] + i[671])",
        "j['PRI_1'] = (i[531] - i[570]) / (i[531] + i[570])",
        "j['PRI_2'] = (i[570] - i[531]) / (i[570] + i[531])",
        "j['PSND'] = (i[800] - i[470]) / (i[800] + i[470])",
        "j['PSRI'] = (i[680] - i[500]) / i[750]",
        "j['PSSR_1'] = i[800] / i[676]",
        "j['PSSR_2'] = i[800] / i[635]",
        "j['RE'] = i[750] / i[710]",
        "j['Readone'] = i[415] / i[695]",
        "j['Reflectance_850'] = i[415] / i[695]",
        "j['REIP'] = (700 + 40) * ((0.5 * (i[670] + i[780])- i[700])/ (i[740]) - i[700]))",
        "j['REP_Li'] = (i[670] + i[780]) / 2",
        "j['RES'] = (i[718] - i[675]) / (i[755] - i[675])",
        "j['RGBVI_1'] = (mean(interval(520,560))**0.5 - (mean(interval(430,470)) * mean(interval(630,690))) / (mean(interval(520,560))**0.5 + (mean(interval(430,470)) * mean(interval(630,690)))",
        "j['RGBVI_2'] = (mean(interval(520,560)) - mean(interval(630,690))) / mean(interval(430,470))",
        "j['RGBVI_3'] = (mean(interval(520,560)) + mean(interval(430,470))) / mean(interval(630,690))",
        "j['RGI'] = i[690] / i[550]",
        "j['RI_green'] = ((i[750] - i[800]) - (i[430] - i[470]) / (i[520] - i[585]) - (i[440] - i[480])) - 1",
        "j['RI_red_edge'] = ((i[750] - i[800]) - (i[430] - i[470]) / (i[695] - i[740]) - (i[440] - i[480])) - 1",
        "j['RM'] = (i[750] + i[720]) - 1",
        "j['RNDVI'] = (i[780] - i[670]) / (i[780] + i[670])",
        "j['RDVI'] = (i[800] - i[670]) / (i[800] + i[670])**0.5",
        "j['R_1000_1100'] = i[1000] / i[1100]",
        "j['SAVI'] = (((i[800] - i[680]) * (1 + 0.5))/ (i[800] + i[680] +0.5))",
        "j['SIPI_1'] = (i[800] - i[450]) / (i[800] - i[650])",
        "j['SIPI_2'] = (i[800] - i[450]) / (i[800] - i[680])",
        "j['sPRI_1'] = (j['PRI_1']  + 1) / 2",
        "j['sPRI_2'] = (j['PRI_2']  + 1) / 2",
        "j['SR_1'] = i[900] / i[680]",
        "j['SR_2'] = i[800] / i[680]",
        "j['SR_3'] = i[752] / i[690]",
        "j['SR_4'] = i[750] / i[550]",
        "j['SR_5'] = i[700] / i[670]",
        "j['SR_6'] = i[675] / i[700]",
        "j['SR_7'] = i[750] / i[710]",
        "j['SR_8'] = i[440] / i[690]",
        "j['SR_9'] = i[515] / i[550]",
        "j['SR_10'] = i[445] / i[800]",
        "j['SR_11'] = i[487] / i[705]",
        "j['SR_11'] = i[750] / i[705]",
        "j['SR_12'] = i[750] / i[700]",
        "j['SR_13'] = i[810] / i[560]",
        "j['SRPI'] = i[430] / i[680]",
        "j['SRWI_1'] = i[858] / i[1240]",
        "j['SRWI_2'] = i[850] / i[1240]",
        "j['SWWI'] = (i[850] - i[1650]) / (i[850] + i[1650])",
        "j['S2TCI'] = (i[740] - i[705]) / (i[705] - i[665])",
        "j['TCARI_1'] = 3 * ((i[700] - i[670]) - 0.2 * (i[700] - i[550]) * (i[700] / i[670]))",
        "j['TCARI_2'] = 3 * ((i[750] - i[705]) - 0.2 * (i[750] - i[550]) * (i[750] / i[705]))",
        "j['TSAVI'] = 1.4735*(i[780] + 1.4735 * i[650] - 1.3681) / (- 1.4735 * i[780] + i[650] + 1.4735 * 1.3681) ",
        "j['TGI'] = -0.5 * (190 * (i[670] - (i[550]) - 120 * (i[670]) - (i[480]))",
        "j['TVI'] = 0.5 * (120 * (i[750]) - (i[550]) - 200 * (i[670]) - i[550]))",
        "j['WBI_1'] = i[950] / i[900]",
        "j['WBI_2'] = i[900] / i[1530]",
        "j['WBI_D'] = (i[1640] - i[482]) / (i[1640] + i[482])",
        "j['WEI'] = ((i[755] + i[680] 2 * i[705]) * min * (mean(interval(930,980)) / (mean(interval(755,680) * i[900])",
        "j['WI'] = i[900] / i[970]",
        "j['WI_hNDVI'] = (i[900] / i[970]) / ((i[900] - i[680]) / (i[900] - i[680]))",
        "j['WDVI'] = i[830] - 1.06 * i[660]",
        "j['VRI_1'] = i[740] / i[720]",
        "j['VRI_2'] = (i[734] - i[747]) / (i[715] + i[726])",
        "j['VRI_3'] = i[715] / i[705]",
        "j['VRI_4'] = (i[734] - i[747]) / (i[715] + i[720])",
        "j['VARI_1'] = (mean(interval(520,560)) - mean(interval(630,690))) / (mean(interval(520,560)) + mean(interval(630,690)) - mean(interval(430,470)))",
        "j['VARI_2'] = (i[550] - i[670]) / (i[550] + i[670])", 
        "j['VARI_3'] = (mean(interval(520,560)) - j['VARI_1']) / (mean(interval(520,560)) + j['VARI_1'] + mean(interval(430,470)))", 
        "j['bNDVI_VARI'] = (j['bNDVI'] - j['VARI_2']) / (j['bNDVI'] + j['VARI_2'])",
        "j['VARI_VARI1'] = (j['VARI_3'] - j['VARI_1']) / (j['VARI_3'] + j['VARI_1'])"]
        
        # Galvincio et al. (2012) -> j['GPP_umol_m-2_s-1']
        # Richardson & Wiegand (1977) -> j['WDVI']
        # Liu et al. (2004) -> j['WI']

        for m in o:
            try:
                exec(m)
            except:
                m = m.split("=")[0] + "='ERROR'"
                exec(m)

def main():
    # this exports the indices
    # into a csv file
    def export(signatures):
        with asksaveasfile(mode='w', defaultextension='.csv', filetypes=[('.csvfile', '.csv')], title='Selecionar arquivo de resultados') as writer:
            for i in signatures:
                # this writes first line: names of the indices
                if i == signatures[0]:
                    keys = [''] + list(i.indices.keys()) + ['\n']
                    writer.write(",".join(keys))
                # this writes the other lines
                header = str(i.header).replace('\n', '')    # this gets the name of the file or signature
                x = [header] + list(map(str, i.indices.values())) + ['\n']    # this gets the data of each index
                writer.write(",".join(x))

    # this opens the first
    # window that asks for
    # the input file
    Tk().withdraw()
    file = askopenfilename(filetypes=[('.ViewSpec','.dat'), ('.ViewSpec','.txt')], title='Abrir arquivo do ViewSpec')
    tkMessageBox.showwarning("Aviso", "Por favor espere uma segunda janela abrir.")

    # this creates the
    # signatures list
    signatures = []

    # this part tries 
    # to load the
    # dataset
    try:
        reader = io.open(file, 'r', encoding='utf-16').readlines() # this handles utf-16 encoded files
    except:
        reader = io.open(file, 'r', encoding='utf-8').readlines() # this handles utf-8 encoded files

    for i in range(len(reader[0].split('\t')[1:])):    # this iterates through the columns
        signature = ViewSpecPy()  # this creates the ViewSpecPy object
        signature.load(reader, i)    # this starts populating the signature.dict
        signature.process()  # this starts populating the signature.indices
        signatures.append(signature) # this adds the ViewSpecPy object to the signatures list

    # this exports the
    # content of the
    # signatures list
    export(signatures)


main()