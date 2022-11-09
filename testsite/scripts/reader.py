from rdkit import Chem
from rdkit.Chem import Draw
from Reader.models import Substance
import re
import os
from pathlib import Path
import PIL.Image as Image
import io

'''os.environ.setdefault('DJANGO_SETTINGS_MODULE','testsite.settings')
django.setup()'''

def run():
    database_dir = './scripts/data/'
    dir = os.fsencode(database_dir)
    file_list = [f for f in Path(database_dir).glob('**/*') if f.is_file()]
    print(file_list)
    for file in file_list:
        filename = os.fsdecode(file)
        if filename.endswith(".sdf"):
            with Chem.SDMolSupplier(filename) as suppl:
                for substance in suppl:
                    if substance is None: continue
                    subst = Substance()
                    subst.PubChem_CID = substance.GetProp('PUBCHEM_COMPOUND_CID')
                    subst.PubChem_Name = substance.GetProp('PUBCHEM_IUPAC_NAME')
                    subst.PubChem_Alias = substance.GetProp('PUBCHEM_IUPAC_NAME')
                    subst.PubChem_Formula = substance.GetProp('PUBCHEM_MOLECULAR_FORMULA')
                    subst.PubChem_Mass = substance.GetProp('PUBCHEM_MOLECULAR_WEIGHT')
                    local_dir = './media/{}.png'.format(substance.GetProp('PUBCHEM_COMPOUND_CID'))
                    Draw.MolToFile(substance,local_dir)
                    img = Image.open(local_dir)
                    iob = io.BytesIO()
                    subst.Local_Image.save('./media/'+local_dir,iob)
                    subst.save()
