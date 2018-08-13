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

class MainVC: NSViewController, MKMapViewDelegate {
    // variables
    var isRunning = false
    var outputPipe:Pipe!
    var proc:Process!
    var startPoint : NSPoint!
    var startCoord, endCoord : CLLocationCoordinate2D!
    var shapeLayer : CAShapeLayer!

    
    // outlets
    @IBOutlet weak var spnBusy: NSProgressIndicator!
    //@IBOutlet var txvConsole: NSTextView!
    @IBOutlet weak var dpcStartDate: NSDatePicker!
    @IBOutlet weak var dpcEndDate: NSDatePicker!
    @IBOutlet weak var swtExport: OGSwitch!
    @IBOutlet weak var dslLat: RangeSlider!
    @IBOutlet weak var dslLon: RangeSlider!
    @IBOutlet weak var dslDepth: RangeSlider!
    @IBOutlet weak var mapView: MKMapView!
    

    
    
    
    // actions
    @IBAction func stopProc(_ sender: Any) {
        if isRunning {
            proc.terminate()
        }
    }

    @IBAction func plotTimeSeries(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotTS.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, fname, exportFlag, extV1, extVV1, extV2, extVV2, bundlePath])
    }
    
    @IBAction func plotRegionalMap(_ sender: Any) {
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotRegional.py", tables, vars, date1, lat1, lat2, lon1, lon2, fname, exportFlag, extV1, extVV1, bundlePath])
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
    
    func runScript(_ arguments:[String]) {
        isRunning = true
        let taskQueue = DispatchQueue.global(qos: DispatchQoS.QoSClass.background)
        taskQueue.async {
            guard let path = Bundle.main.path(forResource: "BashScript",ofType:"command") else {
                print("Unable to locate BashScript.command")
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
                })
            }
            
            
            //self.consoleOutput(self.proc)     //console output handling
            self.proc.launch()
            self.proc.waitUntilExit()
        }
    }
    
    func updateQueryParams() {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"

        tables = "tblSST_AVHRR_OI_NRT"
        vars = "sst"
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
        extV1 = "ignore"
        extVV1 = "ignore"
        extV2 = "ignore"
        extVV2 = "ignore"
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

    
    func readCatalog()-> CSVReader {
        //https://github.com/yaslab/CSV.swift
        let file = bundlePath + "/data/catalog.csv"
        let stream = InputStream(fileAtPath: file)!
        let csv = try! CSVReader(stream: stream, hasHeaderRow: true)
        /*
        let header = csv.headerRow
        var counts = 0
        while let row = csv.next() {
            //print("\(row)")
            //print(row[0])
            //counts += 1
        }
        */
        return csv
    }
    
    
    
    
    
    // implemntation
    override func viewDidLoad() {
        super.viewDidLoad()
        Initializer().vcMainInitializer()
        initUI()

        ///////// get cataloge /////////
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
       
        //TODO
        //note that this going to run before the new "catalog" file is retrieved
        //(currently, itis reading the last catalog file)
        readCatalog()
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

