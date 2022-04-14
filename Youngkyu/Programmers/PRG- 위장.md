# #해시 위장

### 문제 정리
<img width="946" alt="image" src="https://user-images.githubusercontent.com/60254939/163393551-b4c223a3-df2e-4bb9-b81a-fab2713521a8.png">
<img width="955" alt="image" src="https://user-images.githubusercontent.com/60254939/163393584-7e922fa6-5a63-4056-964b-b6cf7fc58706.png">



### 풀이



```Swift
import Foundation

unc solution(_ clothes:[[String]]) -> Int {
    var clothesDict: [String:[String]] = [:]
    var clothesNumList: [Int] = []
    
    // 딕셔너리에 옷 종류별로 분류
    // ex) ["headgear": ["yellowhat", "green_turban"], "eyewear": ["bluesunglasses"]]
    clothes.forEach { cloth in
        guard let item = cloth.first else { return }
        guard let kinds = cloth.last else { return }
        
        if (clothesDict[kinds] != nil) {
            clothesDict[kinds]?.append(item)
        } else {
            clothesDict[kinds] = [item]
        }
    }
    // 옷 종류별 개수 저장 ex) [2, 1]
    clothesDict.forEach { clothesNumList.append($0.value.count) }
    
    return numberOfCase(numbers: clothesNumList)
}

func numberOfCase(numbers: [Int]) -> Int {
    return numbers.reduce(1) { $0 * ($1 + 1) } - 1
}

```

문제를 읽자마자 딕셔너리와 경우의 수를 활용하는 문제임을 직감했다.

딕셔너리를 통해 옷을 종류별로 분류한 다음, 각 종류 별 count를 저장하면

이 count들을 경우의 수를 계산하는 알고리즘에 적용하면 풀리겠다고 생각했다.

그러나 한시간이 넘어도 경우의 수를 구할 방법이 떠오르지 않아 구글의 힘을 빌려 계산했다..

경우의 수 계산 정리

기본적인 경우의 수를 계산하는 방법대로 a종류의 옷 M개 * b종류의 옷 N개 를 하면 

모든 종류의 옷을 하나씩 골라야 했을때의 경우의 수가 됨!!

하지만 이 문제에선 파란 선글라스만 끼고 나체상태도 가능한 변태 스파이라

선택을 안했을 때의 경우의 수를 추가하기 위해 (M+1) * (N+1) 이 됨 !

그리고 아무것도 선택하지 않는 경우의 수(나체상태 스파이) 를 빼기 위해 (M+1) * (N+1) - 1 이 됨!





### 풀고나서 알게된 것

알고리즘 문제들을 풀다보니 경우의 수, 조합 등을 사용하는 문제가 많은 것 같다ㅜㅜ

방구석 어딘가에 있을 개념원리를 찾아봐야 되나.. 
