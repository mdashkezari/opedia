//
//  Initialize.swift
//  opedia
//
//  Created by Mohammad Dehghani Ashkezari on 2018-06-11.
//  Copyright © 2018 Mohammad Dehghani Ashkezari. All rights reserved.
//

import Foundation
import Cocoa

class Initializer {
    
    
    func exists(_ path: String)->(Bool, Bool) {
        var dir = false
        var file = false
        let fileManager = FileManager.default
        var isDir : ObjCBool = false
        if fileManager.fileExists(atPath: path, isDirectory:&isDir) {
            if isDir.boolValue {dir = true} else {file = true}
        }
        return (dir, file)
    }
    
    func msgDialog(headline: String, text: String) -> Bool {
        let alert = NSAlert()
        alert.messageText = headline
        alert.informativeText = text
        alert.alertStyle = .critical
        alert.addButton(withTitle: "OK")
        alert.addButton(withTitle: "Cancel")
        return alert.runModal() == .alertFirstButtonReturn
    }
    
  

    func setBundlePath(){
        let url = URL(fileURLWithPath: Bundle.main.bundlePath)
        bundlePath = url.deletingLastPathComponent().path
    }
    
        
    func setPythonPath() {
        let fm = FileManager.default
        let homeDir = fm.homeDirectoryForCurrentUser.path
        let pythonRootPath2 = "/anaconda2/bin/python"
        let pythonUserPath2 = homeDir + pythonRootPath2
        let pythonRootPath3 = "/anaconda3/bin/python"
        let pythonUserPath3 = homeDir + pythonRootPath3
        
        if exists(pythonUserPath3).1 {pythonPath = pythonUserPath3}
        else if exists(pythonRootPath3).1 {pythonPath = pythonRootPath3}
        else if exists(pythonUserPath2).1 {pythonPath = pythonUserPath2}
        else if exists(pythonRootPath2).1 {pythonPath = pythonRootPath2}
        else {
            _ = msgDialog(headline: "Unable to locate any anaconda distribution. \n Install python anaconda distribution.", text: "Expecting either: \n" + pythonUserPath3 + " \n or \n " + pythonRootPath3 + " \n or \n " + pythonUserPath2 + " \n or \n " + pythonRootPath2)
            NSApplication.shared.terminate(self)
        }
        
    }
    
    
    func writeFile(text: String, to filePath: String) {
        try? text.write(to: URL(fileURLWithPath: filePath), atomically: false, encoding: String.Encoding.utf8)
    }

    
}
