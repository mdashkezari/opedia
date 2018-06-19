//
//  Initialize.swift
//  opedia
//
//  Created by Mohammad Dehghani Ashkezari on 2018-06-11.
//  Copyright © 2018 Mohammad Dehghani Ashkezari. All rights reserved.
//

import Foundation

class Initializer {

    func vcMainInitializer(){
        pythonPath = "/anaconda2/bin/python"
        opediaAPI = "/anaconda2/lib/python2.7/site-packages/opedia/"
        
        let url = URL(fileURLWithPath: Bundle.main.bundlePath)
        bundlePath = url.deletingLastPathComponent().path

    }
}
