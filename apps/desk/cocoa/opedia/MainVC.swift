//
//  MainVC.swift
//  opedia
//
//  Created by Mohammad Dehghani Ashkezari on 2018-06-11.
//  Copyright © 2018 Mohammad Dehghani Ashkezari. All rights reserved.
//

import Cocoa
import OGSwitch
import CSV
import MapKit
import QuartzCore

class MainVC: NSViewController, MKMapViewDelegate, NSTokenFieldCellDelegate, NSTokenFieldDelegate {
    // MARK: - strucs
    struct cat {
        var short_name: String
        var long_name: String
        var make: String
        var sensor: String
        var table_name: String
        var keywords: String
        var ID: Int
    }

    // MARK: - variables
    var isRunning = false
    var outputPipe:Pipe!
    var proc:Process!
    var startPoint : NSPoint!
    var startCoord, endCoord : CLLocationCoordinate2D!
    var shapeLayer : CAShapeLayer!
    var catItems = [cat]()
    
    
    // MARK: - outlets
    @IBOutlet weak var spnBusy: NSProgressIndicator!
    //@IBOutlet var txvConsole: NSTextView!
    @IBOutlet weak var dpcStartDate: NSDatePicker!
    @IBOutlet weak var dpcEndDate: NSDatePicker!
    @IBOutlet weak var swtExport: OGSwitch!
    @IBOutlet weak var dslLat: RangeSlider!
    @IBOutlet weak var dslLon: RangeSlider!
    @IBOutlet weak var dslDepth: RangeSlider!
    @IBOutlet weak var mapView: MKMapView!
    @IBOutlet var acCatalog: NSArrayController!
    @IBOutlet weak var tokenField: NSTokenField!
    

    
    
    
    // MARK: - actions
    @IBAction func stopProc(_ sender: Any) {
        if isRunning {
            proc.terminate()
        }
    }

    @IBAction func plotTimeSeries(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotTS.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }
    
    @IBAction func plotRegionalMap(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotRegional.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }

    @IBAction func plotMutualTrend(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotXY.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, fname, exportFlag, extV1, extVV1, extV2, extVV2, bundlePath])
    }


    @IBAction func plotHist(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotDist.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }
    

    @IBAction func plotDepthProfile(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotDepthProfile.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }

    
    @IBAction func plotSection(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotSection.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }

    
    /*
    func consoleOutput(_ task:Process) {
        outputPipe = Pipe()
        task.standardOutput = outputPipe
        outputPipe.fileHandleForReading.waitForDataInBackgroundAndNotify()
        NotificationCenter.default.addObserver(forName: NSNotification.Name.NSFileHandleDataAvailable, object: outputPipe.fileHandleForReading , queue: nil) {
            notification in
            let output = self.outputPipe.fileHandleForReading.availableData
            let outputString = String(data: output, encoding: String.Encoding.utf8) ?? ""
            DispatchQueue.main.async(execute: {
                let previousOutput = self.txvConsole.string ?? ""
                let nextOutput = previousOutput + "\n" + outputString
                self.txvConsole.string = nextOutput
                let range = NSRange(location:nextOutput.characters.count,length:0)
                self.txvConsole.scrollRangeToVisible(range)
            })
            self.outputPipe.fileHandleForReading.waitForDataInBackgroundAndNotify()
        }
    }
    */
    
    func initUI() {
        swtExport.isOn = false
        swtExport.reloadLayer()

        tokenField.objectValue = []
        
        dslLat.colorStyle = .aqua
        dslLat.knobStyle = .circular
        dslLat.minValue = -90
        dslLat.maxValue = 90
        dslLat.start = 20
        dslLat.end = 45

        dslLon.colorStyle = .aqua
        dslLon.knobStyle = .circular
        dslLon.minValue = -180
        dslLon.maxValue = 180
        dslLon.start = -180
        dslLon.end = -125

        dslDepth.colorStyle = .aqua
        dslDepth.knobStyle = .circular
        dslDepth.minValue = 0
        dslDepth.maxValue = 5727
        dslDepth.start = 0
        dslDepth.end = 5727
    }
    
    
    func runScript(_ arguments:[String], _ async: Bool=true) {
        func runProc() {
            guard let path = Bundle.main.path(forResource: "BashScript",ofType:"command") else {
                _ = Initializer().msgDialog(headline: "Unable to locate BashScript.command", text: "")
                //print("Unable to locate BashScript.command")
                return
            }
            self.proc = Process()
            self.proc.launchPath = path
            self.proc.arguments = arguments
            self.proc.terminationHandler = {
                task in
                DispatchQueue.main.async(execute: {
                    //self.btnOpedia.isEnabled = true
                    self.spnBusy.stopAnimation(self)
                    self.isRunning = false
                    //// process finished; check if it was asking for catalog
                    if arguments[1].contains("getCatalog") { self.loadCatalog() }
                })
            }
            //self.consoleOutput(self.proc)     //console output handling
            self.proc.launch()
            self.proc.waitUntilExit()
        }
        
        ///////////////////////////////////
        isRunning = true
        let taskQueue = DispatchQueue.global(qos: DispatchQoS.QoSClass.background)
        if async {
            taskQueue.async { runProc() }
        }
        else {
            taskQueue.sync { runProc() }
        }
        ///////////////////////////////////
    }
    
    
    func updateQueryParams() {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"        
        (vars, tables, extV1, extVV1, extV2, extVV2) = parseTokens()
        date1 = formatter.string(from: dpcStartDate.dateValue)
        date2 = formatter.string(from: dpcEndDate.dateValue)
        lat1 = "\(dslLat.start)"
        lat2 = "\(dslLat.end)"
        lon1 = "\(dslLon.start)"
        lon2 = "\(dslLon.end)"
        depth1 = "\(dslDepth.start)"
        depth2 = "\(dslDepth.end)"
        fname = "untitle"
        if swtExport.isOn {
            exportFlag = "1"
        } else {
            exportFlag = "0"
        }
        exportFormat = "csv"
    }

    
    func setSpatialControls(_ coord1: CLLocationCoordinate2D, _ coord2: CLLocationCoordinate2D) {
        if coord1.latitude < coord2.latitude {
            lat1 = "\(coord1.latitude)"
            lat2 = "\(coord2.latitude)"
        } else {
            lat1 = "\(coord2.latitude)"
            lat2 = "\(coord1.latitude)"
        }
        
        if coord1.longitude < coord2.longitude {
            lon1 = "\(coord1.longitude)"
            lon2 = "\(coord2.longitude)"
        } else {
            lon1 = "\(coord2.longitude)"
            lon2 = "\(coord1.longitude)"
        }
        
        dslLat.start = Double(lat1)!
        dslLat.end = Double(lat2)!
        dslLon.start = Double(lon1)!
        dslLon.end = Double(lon2)!

        }
    
    
    func startRegionSelect(_ location: NSPoint) {
        self.startPoint = location //self.view.convert(event.locationInWindow, from: nil)
        
        shapeLayer = CAShapeLayer()
        shapeLayer.lineWidth = 1.0
        shapeLayer.fillColor = NSColor(calibratedRed: 1, green: 0.5, blue: 0, alpha: 0.3).cgColor
        shapeLayer.strokeColor = NSColor(calibratedRed: 1, green: 0.5, blue: 0, alpha: 1).cgColor
        shapeLayer.lineDashPattern = [10,5]
        mapView.layer?.addSublayer(shapeLayer)
        
        var dashAnimation = CABasicAnimation()
        dashAnimation = CABasicAnimation(keyPath: "lineDashPhase")
        dashAnimation.duration = 0.75
        dashAnimation.fromValue = 0.0
        dashAnimation.toValue = 15.0
        dashAnimation.repeatCount = .infinity
        shapeLayer.add(dashAnimation, forKey: "linePhase")
    }
    
    func drawRect(_ location: NSPoint) {
        let point : NSPoint = location
        let path = CGMutablePath()
        path.move(to: self.startPoint)
        path.addLine(to: NSPoint(x: self.startPoint.x, y: point.y))
        path.addLine(to: point)
        path.addLine(to: NSPoint(x:point.x,y:self.startPoint.y))
        path.closeSubpath()
        self.shapeLayer.path = path
    }
    
    func endRegionSelect() {
        if self.shapeLayer != nil {
            self.shapeLayer.removeFromSuperlayer()
            self.shapeLayer = nil
        }
    }
    
    @objc func mapPanned(recognizer: NSClickGestureRecognizer) {
        let location = recognizer.location(in: mapView)
        let coordinates = mapView.convert(location, toCoordinateFrom: mapView)
        
        switch recognizer.state {
        case .began:
            startCoord = coordinates
            startRegionSelect(location)
        case .changed:
            setSpatialControls(startCoord, coordinates)
            drawRect(location)
        case .ended:
            endCoord = coordinates
            setSpatialControls(startCoord, endCoord)
            endRegionSelect()
        default:
            endRegionSelect()
        }
    }

    
    func loadCatalog()-> CSVReader {
        //https://github.com/yaslab/CSV.swift
        let file = bundlePath + "/data/catalog.csv"
        let stream = InputStream(fileAtPath: file)!
        let csv = try! CSVReader(stream: stream, hasHeaderRow: true)
        //let header = csv.headerRow
        
        while let row = csv.next() {
            // fill cat struct
            catItems.append(cat(short_name: row[0], long_name: row[1], make: row[3], sensor: row[4], table_name: row[16], keywords: row[17], ID: Int(row[15])! ))
            /*
            // fill catalog array controller
            self.acCatalog.addObject(
                CatalogVar(short_name: row[0],
                           long_name: row[1],
                           unit: row[2],
                           make: row[3],
                           sensor: row[4],
                           process_level: row[5],
                           study_domain: row[6],
                           temporal_resolution: row[7],
                           spatial_resolution: row[8],
                           dataset_name: row[10],
                           data_source: row[11],
                           distributor: row[12],
                           id: row[15],
                           table_name: row[16],
                           keywords: row[17]
            )
            )
             */
        }
        return csv
    }
    
    
    func extractTokenID(_ tokenValue: String)->Int? {
        let prefix = " ID("
        if tokenValue.contains(prefix) == false {return nil}
        let start = tokenValue.range(of: prefix)?.upperBound
        let end = tokenValue.index(before: tokenValue.endIndex)
        let ID = tokenValue[start!..<end]
        return Int(ID)
    }
    
    func getTokenIDs() -> [Int]{
        var res = [Int]()
        let tokenCounts = (tokenField.objectValue as! NSArray).count
        if tokenCounts<1 {return res}
        for i in 0...tokenCounts-1 {
            if let ID = extractTokenID((tokenField.objectValue as! NSArray)[i] as! String) {
                res.append(ID)
            } else {continue}
        }
        return res
    }
    
    func parseTokens() -> (String, String, String, String, String, String) {
        var vars: String = ""
        var tables: String = ""
        var extVs: String = ""
        var extVVs: String = ""
        var extVs2: String = ""
        var extVVs2: String = ""

        var extV: String = ""
        var extVV: String = ""
        var extV2: String = ""
        var extVV2: String = ""

        let IDs = getTokenIDs()
        if IDs.count<1 {return (vars, tables, extVs, extVVs, extVs2, extVVs2)}
        
        for i in 0...IDs.count-1 {
            let token = catItems.filter({return $0.ID == IDs[i]})
            vars += token[0].short_name
            tables += token[0].table_name
            
            extV = "ignore"
            extVV = "ignore"
            extV2 = "ignore"
            extVV2 = "ignore"
            if token[0].table_name.contains("Wind") {
                extV = "hour"
                extVV = "12"
                extV2 = "hour"
                extVV2 = "12"
            }
            if token[0].table_name.contains("Pisces") ||
               token[0].table_name.contains("Darwin") ||
               token[0].table_name.contains("tblHOT_") ||
               token[0].table_name.contains("tblCobalamin") ||
               token[0].table_name.contains("tblArgo") {
                
                extV = "depth"
                extVV = "\(dslDepth.start)"
                extV2 = "depth"
                extVV2 = "\(dslDepth.end)"
            }

            extVs += extV
            extVVs += extVV
            extVs2 += extV2
            extVVs2 += extVV2
            
            if i<IDs.count-1 {
                vars += ","
                tables += ","
                extVs += ","
                extVVs += ","
                extVs2 += ","
                extVVs2 += ","

            }
        }
        return (vars, tables, extVs, extVVs, extVs2, extVVs2)
    }
    
    
    func opediaPathScript() -> String {
        return """
        import site
        file = open("out.txt","w")
        path = site.getsitepackages()[-1]
        file.write(path + "/opedia/")
        """
    }
    
    
    func setOpediaAPI() {
        ///////// set opediaAPI (path to opedia python package) /////////
        let opPackScript: String = bundlePath+"/opPack.py"
        Initializer().writeFile(text: opediaPathScript(), to: opPackScript)
        runScript([pythonPath, opPackScript, bundlePath], false)
        opediaAPI = try! NSString(contentsOfFile: bundlePath+"/out.txt", encoding: String.Encoding.utf8.rawValue) as String
        do {
            let fm = FileManager.default
            try fm.removeItem(atPath: bundlePath+"/out.txt")
            try fm.removeItem(atPath: bundlePath+"/opPack.py")
        }
        catch let error as NSError {
            print("Error while deleteing python file: \(error)")
        }
    }
    
    
    
    
    
    // MARK: - implemntation
    override func viewDidLoad() {
        super.viewDidLoad()
        initUI()
        Initializer().setBundlePath()
        Initializer().setPythonPath()
        setOpediaAPI()

        ///////// get cataloge /////////
        spnBusy.startAnimation(self)
        runScript([pythonPath, "\(opediaAPI)getCatalog.py", bundlePath])
        ////////////////////////////////
        
        /////// gesture recognizer /////
        let panRecognizer = NSPanGestureRecognizer(target: self, action: #selector(mapPanned))
        panRecognizer.buttonMask = 2
        mapView.addGestureRecognizer(panRecognizer)
        ///////////////////////////////
    }
    
    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }

    override func viewDidAppear() {
        //view.window?.makeFirstResponder(self)
        // loadCatalog()
    }
    

    func tokenField(_ tokenField: NSTokenField, completionsForSubstring substring: String, indexOfToken tokenIndex: Int, indexOfSelectedItem selectedIndex: UnsafeMutablePointer<Int>?) -> [Any]? {
        var res = [String]()
        res = catItems.filter({ return $0.keywords.lowercased().contains(substring.lowercased())}).map({$0.short_name + ": " + $0.long_name + " ID(" + String($0.ID) + ")"})
        res.insert(substring, at: 0)
        return res
        //return (catShortNames as NSArray).filtered(using: NSPredicate(format: "SELF beginswith[cd] %@", substring)) as [Any]
    }
    
    func tokenField(_ tokenField: NSTokenField, hasMenuForRepresentedObject representedObject: Any) -> Bool {
        return true
    }
    
    
    
    
    /*
    override func flagsChanged(with event: NSEvent) {
        switch event.modifierFlags.intersection(.deviceIndependentFlagsMask) {
        case [.command]:
            darwSpatial = true
        default:
            darwSpatial = false
        }
    }
    
    */
        
}

