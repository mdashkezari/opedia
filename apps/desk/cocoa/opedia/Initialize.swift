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
        //alert.addButton(withTitle: "Cancel")
        return alert.runModal() == .alertFirstButtonReturn
    }
    
    func vcMainInitializer(){
        
        let pythonPath2 = "/anaconda2/bin/python"
        let opediaAPI2 = "/anaconda2/lib/python2.7/site-packages/opedia/"
        
        let pythonPath3 = "/anaconda3/bin/python"
        let opediaAPI3 = "/anaconda3/lib/python3.6/site-packages/opedia/"
        
        if exists(pythonPath3).1 {
            pythonPath = pythonPath3
            if exists(opediaAPI3).0 {
                opediaAPI = opediaAPI3
            } else {
                let answer = msgDialog(headline: "Opedia python package not found. \n $ pip install opedia", text: "Expecting: \n" + opediaAPI3)
                NSApplication.shared.terminate(self)
            }
        } else if exists(pythonPath2).1 {
            pythonPath = pythonPath2
            if exists(opediaAPI2).0 {
                opediaAPI = opediaAPI2
            } else {
                let answer = msgDialog(headline: "Opedia python package not found. \n $ pip install opedia", text: "Expecting: \n" + opediaAPI2)
                NSApplication.shared.terminate(self)
            }
        } else {
            let answer = msgDialog(headline: "Unable to locate any anaconda distribution. \n Install python anaconda distribution.", text: "Expecting either: \n" + pythonPath2 + " \n or \n " + pythonPath3)
            NSApplication.shared.terminate(self)
        }
        
        let url = URL(fileURLWithPath: Bundle.main.bundlePath)
        bundlePath = url.deletingLastPathComponent().path
        
    }
}
