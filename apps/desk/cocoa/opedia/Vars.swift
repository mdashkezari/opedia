//
//  Vars.swift
//  opedia
//
//  Created by Mohammad Dehghani Ashkezari on 2018-06-11.
//  Copyright © 2018 Mohammad Dehghani Ashkezari. All rights reserved.
//

import Foundation

// opedia API
var pythonPath: String = ""
var opediaAPI: String = ""

// bundle
var bundlePath: String = ""

// dump text file
let dumpFilename = "dump.txt"

// catalog file content
//var catalog: String = ""


// min number of plots that generate a warning message
let plotCountWarning = 20


// if longitude 180 degree has crossed
var crossed180 = false

// query parameters
var tables = ""
var vars = ""
var date1 = ""
var date2 = ""
var lat1 = ""
var lat2 = ""
var lon1 = ""
var lon2 = ""
var depth1 = ""
var depth2 = ""
var fname = ""
var exportFlag = ""
var exportFormat = ""
var invertLon = ""
var extV1 = ""
var extVV1 = ""
var extV2 = ""
var extVV2 = ""


struct delatParams {
    let days: Int
    let lats: Double
    let lons: Double
    let depths: Double
    let depthIndexes: Int
}
