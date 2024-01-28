from collections import defaultdict
import json

data = open("data.json")

data_json = json.load(data)
print(type(data_json))


def sorter (obj):
    sortedData = dict()
    for x,y in obj.items():
        for rows in y:
            # print("1.",rows.keys())
            # break
            if "stand_number" in rows.keys():
                # print("2. aye")
                # print("3. stand_number",rows["stand_number"])
                coords = f"{rows['row_number']}_{x}"
                if  rows['stand_number'] in sortedData.keys():
                    # print("4. ",sortedData[rows['stand_number']])
                    sortedData[rows['stand_number']][1].append(coords)
                else:
                    # print("5.")
                    sortedData[rows['stand_number']] = [rows["color_code"],[]]
                    sortedData[rows['stand_number']][1].append(coords)


                # sortedList.append(coords)

    return(sortedData)

sortedItems = sorter(data_json)
# with open("standWiseData.json","w+") as swd1:
#     swd1.write(json.loads(json.dumps(sortedItems)))
#     swd1.close()

with open("standWiseData.json","w+") as swd1:
    json.dump(sortedItems, swd1)

print(sorter(data_json))
