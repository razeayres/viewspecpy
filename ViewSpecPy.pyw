import io, sys, math
import tkMessageBox
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfile 

class ViewSpecPy(object):
    def __init__(self):
        self.header = ''    # Initializes self.header
        self.dict = {}
        self.indices = {}

    def add(self, t):
        t = t.split(',')
        key = int(float(t[0]))  # To handle the invalid literal for int()
        value = float(t[1])
        self.dict[key] = value

    def load(self, reader, i):
        for j in xrange(len(reader)):   # Iterates through the lines
            # Splits the row
            row = reader[j].split('\t')[1:]
            # Defines the header
            if j == 0:
                self.header = row = row[i]  # Populates self.header
                continue
            # Add the data to the 
            # dict object
            self.add(row[i])    # Populates self.dict
    
    def derivative(self, gap):
        # Calculates the 1st derivative
        i = self.dict.keys()    # Gets the wavelengths
        j = map(float, self.dict.values())  # Gets the values and converts them into float
        m = gap/2   # Gets the median of the gap
        r = []
        for l in xrange(len(self.dict)):
            if (l+1 <= m) or (l+1 >= (len(self.dict) - m)):
                # Fill the values before
                # (at the begining)
                # and after (at the end)
                # the median of the gap
                # as 0 (zero)
                r.append(0)
            else:
                # Calculates 1st
                # derivative data
                x = (j[l-m] - j[l+m]) / (i[l-m] - i[l+m])
                x = round(x, 3) # Rounds the value to a 3 decimal number
                r.append(x)
        return r

    def process(self):
        i = self.dict
        j = self.indices
        l = self.derivative(7)

        mn = min(i.keys())
        mx = max(i.keys())

        o = []

        # Populates self.indices
        # Add new indices here:
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
    # Exports the indices
    # into a csv file
    def export(signatures):
        with asksaveasfile(mode='w', defaultextension='.csv', filetypes=[('.csvfile', '.csv')], title='Selecionar arquivo de resultados') as writer:
            for i in signatures:
                # Writes first line: names of the indices
                if i == signatures[0]:
                    keys = [''] + i.indices.keys() + ['\n']
                    writer.write(",".join(keys))
                # Writes the other lines
                header = str(i.header).replace('\n', '')    # Gets the name of the file or signature
                x = [header] + map(str, i.indices.values()) + ['\n']    # Gets the data of each index
                writer.write(",".join(x))

    Tk().withdraw()
    file = askopenfilename(filetypes=[('.ViewSpec','.dat'), ('.ViewSpec','.txt')], title='Abrir arquivo do ViewSpec')
    tkMessageBox.showwarning("Aviso", "Por favor espere uma segunda janela abrir.")

    signatures = [] # Creates signatures list
    try:
        reader = io.open(file, 'r', encoding='utf-16').readlines() # Handles utf-16 encoded files
    except:
        reader = io.open(file, 'r', encoding='utf-8').readlines() # Handles utf-8 encoded files
    for i in xrange(len(reader[0].split('\t')[1:])):    # Iterates through the columns
        signature = ViewSpecPy()  # Creates the ViewSpec object
        signature.load(reader, i)    # Start signature.dict populating
        signature.process()  # Start signature.indices populating
        signatures.append(signature) # Adds the ViewSpec object to signatures list

    export(signatures)


main()