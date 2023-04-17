import time
import json
import os
from .util import write_json, is_enabled, disable, versions


def manipulacion(split):
    temp = split.pop(0)
    new = ""

    for x in split:
        new += x
        new += " "
    new = new[:-1]
    if temp == "put":
        new = new.split(", ")
        if not is_enabled(new[0].replace("'", "")):
            return "Tabla esta desactivada"
        a_file = open('./data/'+new[0].replace("'", "")+".json")
        json_object = json.load(a_file)
        a_file.close()
        row = False
        x = None
        for p in json_object:
            if new[1] in p:
                row = True
                x = p
        if row:

            JSON = x[new[1]]
            v = versions(new[0].replace("'", ""))

            column = new[2].split(":")

            if column[0].replace("'", "") in json_object[0]:

                if column[0].replace("'", "") not in JSON:
                    JSON[column[0].replace("'", "")] = {}
                a = JSON[column[0].replace("'", "")]
                if column[1].replace("'", "") not in a:
                    a[column[1].replace("'", "")] = []
                temp = a[column[1].replace("'", "")]

                temp.append({"value": new[3].replace(
                    "'", ""), "timestamp": time.time()})
                if len(temp) == v:
                    temp.pop(0)
                x = JSON
            else:
                print("Columna no Existe")

        else:
            JSON = {}
            column = new[2].split(":")
            if column[0].replace("'", "") in json_object[0]:
                JSON[column[0].replace("'", "")] = {column[1].replace("'", ""): [
                    {"value": new[3].replace("'", ""), "timestamp": time.time()}]}
                BIG = {new[1].replace("'", ""): JSON}
                json_object.append(BIG)
            else:
                print("Columna no existe")
        filename = new[0].replace("'", "")
        write_json(filename, json_object)
    elif temp == "get":
        new = new.replace("'", "").split(", ")
        if not is_enabled(new[0].replace("'", "")):
            return "Tabla esta desactivada"
        a_file = open('./data/'+new[0]+".json")
        json_object = json.load(a_file)
        a_file.close()
        columnas = None
        version = None
        if len(new) >= 3:
            if len(new) == 3:
                if "{" not in new[2] or "}" not in new[2] or "=>" not in new[2]:
                    return "Error de Sintaxis"
            elif len(new) == 4:
                if "{" not in new[2] or "}" not in new[3] or "=>" not in new[2] or "=>" not in new[3]:
                    return "Error de Sintaxis"
                p = new[3].split("=>")
                version = int(p[1].replace("}", "").replace(" ", ""))
                if p[0].replace("}", "").replace(" ", "") != "VERSIONS":
                    return "Error de Sintaxis"
            columnas = new[2].split("=>")

            
            columnas[0] = columnas[0].replace("{", "").replace(" ", "")
            columnas[1] = columnas[1].replace("}", "")
            columnas[1] = columnas[1][1:]
            if columnas[0] != "COLUMN":
                return "Error de sintaxis"

        print("COLUMN               CELL")
        for x in json_object:
            if new[1] in x:
                JSON = x[new[1]]
                for y in JSON:
                    newjson = JSON[y]
                    for z in JSON[y]:
                        if version:
                            jsons = newjson[z]
                            if columnas != None:
                                data = columnas[1].split(":")
                                if y == data[0] and z == data[1]:
                                    for m in jsons:
                                        print(str(z)+":"+str(y), "       timestamp=" +
                                              str(m["timestamp"]) + "  value="+str(m["value"]))
                            else:
                                for m in jsons:
                                    print(str(z)+":"+str(y), "         timestamp=" +
                                          str(m["timestamp"]) + "  value="+str(m["value"]))
                        else:
                            jsons = newjson[z][0]
                            if columnas != None:
                                data = columnas[1].split(":")
                                if y == data[0] and z == data[1]:
                                    print(str(z)+":"+str(y), "       timestamp=" +
                                          str(jsons["timestamp"]) + "  value="+str(jsons["value"]))
                            else:
                                print(str(z)+":"+str(y), "         timestamp=" +
                                      str(jsons["timestamp"]) + "  value="+str(jsons["value"]))
    elif temp == "scan":
        new = new.replace("'", "").split(", ")
        if not is_enabled(new[0].replace("'", "")):
            return "Tabla esta desactivada"
        a_file = open('./data/'+new[0]+".json")
        json_object = json.load(a_file)
        a_file.close()
        print("ROW            COLUMN+CELL")
        json_object.pop(0)
        for x in json_object:
            for y in x:
                rows = x[y]
                for z in rows:
                    columns = rows[z]
                    for w in columns:
                        values = columns[w]
                        values = values[0]
                        print(str(y) + "              column="+str(z)+":"+str(w) + ", " +
                              "timestamp="+str(values["timestamp"])+", " + "value="+str(values["value"]))

    elif temp == "delete":
        new = new.replace("'", "").split(", ")
        if not is_enabled(new[0].replace("'", "")):
            return "Tabla esta desactivada"
        a_file = open('./data/'+new[0]+".json")
        json_object = json.load(a_file)
        a_file.close()
        for x in json_object:
            if new[1] in x:
                JSON = x[new[1]]
                column = new[2].split(":")
                a = JSON[column[0].replace("'", "")]
                if len(new) == 4:
                    te = []
                    for x in a[column[1].replace("'", "")]:
                        if x['timestamp'] == float(new[3].replace("'", "")):
                            continue
                        else:
                            te.append(x)
                    a[column[1].replace("'", "")] = te
                else:
                    del a[column[1].replace("'", "")]
                x = JSON
        a_file = open('./data/'+new[0].replace("'", "")+".json", "w")
        json.dump(json_object, a_file)
        a_file.close()
    elif temp == "deleteAll":
        new = new.replace("'", "").replace(",", "").split()
        if not is_enabled(new[0].replace("'", "")):
            return "Tabla esta desactivada"
        a_file = open('./data/'+new[0]+".json")
        json_object = json.load(a_file)
        a_file.close()
        for x in json_object:
            if new[1] in x:
                json_object.remove(x)
        a_file = open('./data/'+new[0].replace("'", "")+".json", "w")
        json.dump(json_object, a_file)
        a_file.close()
    elif temp == "count":
        if not is_enabled(new.replace("'", "")):
            return "Tabla esta desactivada"
        a_file = open('./data/'+new.replace("'", "")+".json")
        json_object = json.load(a_file)
        a_file.close()
        json_object.pop(0)
        print(len(json_object))
    elif temp == "truncate":
        a_file = open('./data/'+new.replace("'", "")+".json")
        json_object = json.load(a_file)
        a_file.close()
        disable(new.replace("'", ""))
        print("Tabla desactivada")
        print("Dropping tabla")
        a_file = open('./data/'+new.replace("'", "")+".json", "w")
        json.dump([json_object[0]], a_file)
        a_file.close()
