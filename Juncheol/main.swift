//
//  main.swift
//  ReadLine
//
//  Created by 김준철 on 2022/03/31.
//
import Foundation


var a = readLine();

if let a = a{
    let array = a.components(separatedBy: " ")
    if let val1 = Int(array[0]), let val2 = Int(array[1]) {
        let sol = val1 + val2
        print(sol)
    }
