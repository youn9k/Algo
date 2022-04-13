# #2022 KAKAO BLIND RECRUITMENT 신고 결과 받기

### 문제 정리
<img width="577" alt="image" src="https://user-images.githubusercontent.com/60254939/162983681-ae565f02-5e97-440d-a325-6e8675651d27.png">
<img width="572" alt="image" src="https://user-images.githubusercontent.com/60254939/162983786-ac5892c8-a1af-4d23-a0a0-811a2cfa274b.png">
<img width="573" alt="image" src="https://user-images.githubusercontent.com/60254939/162983871-4ddbd174-aa77-471f-bf7b-6917081858ac.png">
<img width="571" alt="image" src="https://user-images.githubusercontent.com/60254939/162983908-cd183f3d-5c07-458d-a40c-3fbd98750401.png">



### 풀이



```Swift
import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {

    let uniqueReport = Array(Set(report)) // 동일 유저에 대한 신고 중복 제거
    var reportIDs: [String] = [] // 신고한 유저
    var reportedIDs: [String] = [] // 신고당한 유저
    var blackList: [String] = [] // 제재확정 유저 명단
    var mailList: [String] = [] // 결과 메일을 받을 유저 명단
    var mailCount: [Int] = [] // 결과 메일을 받을 횟수

    // " "를 기준으로 신고한 유저, 신고당한 유저 분리
    reportIDs = uniqueReport.map { String($0.split(separator: " ").first!) }
    reportedIDs = uniqueReport.map { String($0.split(separator: " ").last!) }

    
    reportedIDs.indices.forEach { i in
        // k번 이상 신고당한 유저는 블랙리스트에 추가
        if reportedIDs.filter({ $0 == reportedIDs[i] }).count >= k {
            blackList.append(reportedIDs[i])
        }
        // 신고 당한 유저가 블랙리스트라면 메일을 받을 유저 명단에 추가
        if blackList.contains(reportedIDs[i]) {
            mailList.append(reportIDs[i])
        }
    }
    
    // 메일 받을 명단의 유저를 세서 mailCount에 추가
    id_list.indices.forEach { i in
        mailCount.append( mailList.filter({ $0 == id_list[i] }).count )
    }

    print("reportIDs:", reportIDs) // reportIDs: ["muzi", "apeach", "apeach", "frodo", "muzi"]
    print("reportedIDs", reportedIDs) // reportedIDs ["frodo", "frodo", "muzi", "neo", "neo"]
    print("blackList", blackList) // blackList ["frodo", "frodo", "neo", "neo"]
    print("mailList", mailList) // mailList ["muzi", "apeach", "frodo", "muzi"]
    print(mailCount) // [2, 1, 1, 0]

    return mailCount
}

```

```Swift
        // 신고 당한 유저가 블랙리스트라면 메일을 받을 유저 명단에 추가
        if blackList.contains(reportedIDs[i]) {
            mailList.append(reportIDs[i])
        }
```

이 부분이 어려웠는데, 내가 가진 정보는 신고한 유저, 신고당한 유저, 블랙리스트 3가지밖에 없는데 어떻게 메일을 받을 유저를 순서대로 정렬할 수 있을까 고민이 많았다.

긴 고민끝에 생각한 방법은

"무지가 프로도를 신고했다" 라는 문장은 "muzi frodo" 가 되고 ```reportIDs[i], reportedIDs[i]``` 로 표현할 수 있었다.

따라서 for문 안에서 i번째 ```reportIDs[i], reportedIDs[i]``` 는 문장의 연관성이 있었기에

**i번째 신고 당한 유저**가 블랙리스트에 있다면 **i번째 신고한 유저**가 신고했다는게 보장이 된다. 

(위 주석을 따라가보면 좀 더 이해가 잘될수도..?)


**따라서 위 코드로 블랙리스트와 신고 당한 유저를 활용해 신고한 유저를 찾아낼 수 있었다.**



### 풀고나서 알게된 것

생각보다 너무 어려웠다ㅜㅜ 한참 삽질하다가 결국 질문게시판을 보니 시간초과 관련 질문이 많아 스트림 문법을 최대한 활용하면서 for문을 줄이려고 노력했는데도, 시간초과가 나서 지금으로썬 이게 최선의 코드.. 나중에 다시 한번 풀어봐야지

<img width="541" alt="image" src="https://user-images.githubusercontent.com/60254939/163190344-6b2d3d9d-b8db-4275-88be-67ccd8105669.png">
