from Course8Informatica.jsonHelper import JSONhelper


if __name__ == '__main__':

    jsonboi = JSONhelper()
    jsonboi.append_data("random", "random")
    jsonboi.append_data([1, 2, 3, 4], "random")
    jsonboi.append_data([1, 2, 3, 4, 5], "list")
    jsonboi.append_data([1, 2, 65, 654])
    jsonboi.update({'bob':{'cindy':{'mark':100}}})
    d = jsonboi.fetch(['bob','cindy','mark'])
    print(d)
    print(jsonboi.data())





    # todo cleanup for re-runs
