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
        "j['PRI2'] = (i[570] - i[531]) / (i[570] + i[531])",
        "j['SPRI1'] = (j['PRI1']  + 1) / 2",
        "j['SPRI2'] = (j['PRI2']  + 1) / 2",
        "j['SIPI'] = (i[800] - i[445]) / (i[800] - i[680])",
        "j['ChlNDI'] = (i[750] - i[705]) / (i[750] + i[705])",
        "j['SR705'] = i[750] / i[705]",
        "j['mSR705'] = (i[750] - i[445]) / (i[750] + i[445])",
        "j['NVI'] = (i[777] - i[747]) / i[673]",
        "j['R(red edge)'] = (i[670] + i[780]) / 2",
        "j['NDVI'] = (i[800] - i[670]) / (i[800] + i[670])",
        "j['NDVI2'] = (i[900] - i[680]) / (i[900] + i[680])",
        "j['NPP1_umol_m-2_s-1'] = - (-5.6*(j['NDVI'] * j['SPRI1']) - 0.69)",
        "j['NPP2_umol_m-2_s-1'] = - (-5.6*(j['NDVI'] * j['SPRI2']) - 0.69)",
        "j['CO2_1_umol_m-2_s-1'] = - (-4.3833 - 15.018 * (j['SPRI1'] * j['NDVI']))",
        "j['CO2_2_umol_m-2_s-1'] = - (-4.3833 - 15.018 * (j['SPRI2'] * j['NDVI']))",
        "j['WI'] = i[970] / i[900]",
        "j['NWI1'] = (i[970] - i[900]) / (i[970] + i[900])",
        "j['NWI2'] = (i[970] - i[850]) / (i[970] + i[850])",
        "j['NWI3'] = (i[970] - i[880]) / (i[970] + i[880])",
        "j['NWI4'] = (i[970] - i[920]) / (i[970] + i[920])",
        "j['LAI_Galvincio'] = math.exp(1.426 + (-0.542 / j['NDVI']))",
        "j['WDVI'] = i[830] - 1.06 * i[660]",
        "j['GPP_umol_m-2_s-1'] = (j['WDVI'] + 0.2782) / 0.2137"]

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