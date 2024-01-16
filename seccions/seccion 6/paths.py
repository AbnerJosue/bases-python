from pathlib import Path

base = Path.home()
guia = Path(base,"Barcelona", "Sagrada_Familida")
guia2 = guia.with_name("La_predera.txt")
print(guia)
print(guia2)
print(guia.parent)


guia_path = Path(Path.home(),"Europa")

for txt in Path(guia_path).glob("*.txt"):
    print(txt)