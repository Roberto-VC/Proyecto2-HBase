import time
import json
import os

def manipulacion(split):
    temp = split.pop(0)
    new = ""

    for x in split:
        new += x
        new += " "
        if temp == "put":
            new = new.replace(",", "").split()
            a_file = open(new[0].replace("'", "") + ".json")
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
                column = new[2].split(":")
                if column[0].replace("'", "") in JSON:
                    a = JSON[column[0].replace("'", "")]
                    a[column[1].replace("'", "")] = [
                        new[3].replace("'", ""),
                        time.time(),
                    ]
                    x = JSON
                else:
                    a = {}
                    a[column[1].replace("'", "")] = [
                        new[3].replace("'", ""),
                        time.time(),
                    ]
                    JSON[column[0].replace("'", "")] = a
                    x = JSON
                    print(x)

            else:
                JSON = {}
                column = new[2].split(":")
                JSON[column[0].replace("'", "")] = {
                    column[1].replace("'", ""): [new[3], time.time()]
                }
                BIG = {new[1].replace("'", ""): JSON}
                json_object.append(BIG)
            a_file = open(new[0].replace("'", "") + ".json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            print(json_object)
        elif temp == "get":
            new = new.replace("'", "").replace(",", "").split()
            a_file = open(new[0] + ".json")
            json_object = json.load(a_file)
            a_file.close()
            print(json_object)
            print("COLUMN            CELL")
            for x in json_object:
                if new[1] in x:
                    JSON = x[new[1]]
                    for y in JSON:
                        newjson = JSON[y]
                        for z in JSON[y]:
                            print(z + ":" + y, "value=" + newjson[z][0])
        elif temp == "scan":
            print("ROW            COLUMN+CELL")
            new = new.replace("'", "").replace(",", "").split()
            a_file = open(new[0] + ".json")
            json_object = json.load(a_file)
            a_file.close()
            for x in json_object:
                for y in x:
                    rows = x[y]
                    for z in rows:
                        columns = rows[z]
                        for w in columns:
                            values = columns[w]
                            print(
                                y
                                + "              column="
                                + z
                                + ":"
                                + w
                                + ", "
                                + "timestamp="
                                + values[-1]
                                + ", "
                                + "value="
                                + values[0]
                            )

        elif temp == "delete":
            new = new.replace("'", "").replace(",", "").split()
            a_file = open(new[0] + ".json")
            json_object = json.load(a_file)
            a_file.close()
            for x in json_object:
                if new[1] in x:
                    JSON = x[new[1]]
                    column = new[2].split(":")
                    a = JSON[column[0].replace("'", "")]
                    del a[column[1].replace("'", "")]
                    x = JSON
            print(json_object)
            a_file = open(new[0].replace("'", "") + ".json", "w")
            json.dump(json_object, a_file)
            a_file.close()
        elif temp == "deleteAll":
            new = new.replace("'", "").replace(",", "").split()
            a_file = open(new[0] + ".json")
            json_object = json.load(a_file)
            a_file.close()
            for x in json_object:
                if new[1] in x:
                    json_object.remove(x)
            print(json_object)
            a_file = open(new[0].replace("'", "") + ".json", "w")
            json.dump(json_object, a_file)
            a_file.close()
        elif temp == "count":
            a_file = open(new[0].replace("'", "") + ".json")
            json_object = json.load(a_file)
            a_file.close()
            print(len(json_object))
        elif temp == "truncate":
            a_file = open(new[0].replace("'", "") + ".json")
            json_object = json.load(a_file)
            a_file.close()
            json_object = []
            a_file = open(new[0] + ".json", "w")
            json.dump(json_object, a_file)
            a_file.close()
