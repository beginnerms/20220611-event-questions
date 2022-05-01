def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    
    # 基準値未満のグループ
    below = []
    # 基準値以上のグループ
    above = []
    #探索listの左端のindex
    l = 0
    #探索listの右端のindex
    r = len(array)-1

    # 左端からの探索によるindex番号が右端から探索のindex番号を超えるまで
    while l <= r:
        # 基準値以上の要素と基準値未満の要素を入れ替え
        if array[l] >= pivot and array[r] < pivot:
            below.append(array[r])
            above = [array[l]] + above
            l +=1
            r -=1
        # 右からの探索でその値が基準値以上であれば左隣の要素を探索
        elif array[r] >= pivot:
            above = [array[r]] + above
            r -= 1
        # 左からの探索でその値が基準値未満であれば右隣の要素を探索
        elif array[l] < pivot:
            below.append(array[l])
            l += 1
      
    if below == []:
        below.append(array[0])
        del above[0]

    below = sort(below)
    above = sort(above)

    return below + above

    # ここまで記述

if __name__ == '__main__':
    main()
