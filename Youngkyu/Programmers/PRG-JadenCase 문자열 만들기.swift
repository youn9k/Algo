import Foundation

public func solution(_ s:String) -> String {
    let s = s.components(separatedBy: " ")
    var words: [[Character]] = []
    var upperWords: [[Character]] = []
    var upperSentences = ""
    
    // 전체 소문자로 변경
    // [String] -> [[Character]] 로 변경
    s.map { $0.lowercased() }.forEach { words.append(Array($0)) }

    // 첫 글자만 대문자로 변경
    words.forEach { word in
        var newWord: [Character] = []
        for i in 0..<word.count {
            if i == 0 {
                newWord.append(contentsOf: word[i].uppercased())
            } else {
                newWord.append(word[i])
            }
        }
        upperWords.append(newWord)
    }
  
    // 문자 합치기
    upperWords.forEach { word in
        upperSentences.append(String(word))
        upperSentences.append(" ")
    }
    
    // 마지막 공백 제거
    upperSentences.removeLast()
    
    return upperSentences
}
