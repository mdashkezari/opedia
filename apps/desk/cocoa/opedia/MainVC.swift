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
    
    // space-time tab objects
    @IBOutlet weak var dpcStartDate: NSDatePicker!
    @IBOutlet weak var dpcEndDate: NSDatePicker!
    @IBOutlet weak var swtExport: OGSwitch!
    @IBOutlet weak var dslLat: RangeSlider!
    @IBOutlet weak var dslLon: RangeSlider!
    @IBOutlet weak var dslDepth: RangeSlider!
    @IBOutlet weak var pupStartDepth: NSPopUpButton!
    @IBOutlet weak var pupEndDepth: NSPopUpButton!
    
    // cruise tab objects
    @IBOutlet weak var swtCruise: OGSwitch!
    @IBOutlet weak var pupRegisteredCruise: NSPopUpButton!
    @IBOutlet weak var txfSpatialToleranceCruise: NSTextField!
    @IBOutlet weak var pupSamplingRate: NSPopUpButton!
    @IBOutlet weak var txfVirtualCruise: NSTextField!
    @IBOutlet weak var btnVirtualCruise: NSButton!
    
    // lagrangian tab objects
    @IBOutlet weak var swtTracer: OGSwitch!
    @IBOutlet weak var txtSpatialToleranceTracer: NSTextField!
    
    // eddy tab objects
    @IBOutlet weak var swtAllEddies: OGSwitch!
    @IBOutlet weak var swtEddyPolarity: OGSwitch!
    @IBOutlet weak var txfSpatialToleranceEddy: NSTextField!
    
    // front tab objects
    @IBOutlet weak var swtFTLEType: OGSwitch!
    @IBOutlet weak var swtFTLEBackgroud: OGSwitch!
    @IBOutlet weak var txfSpatialToleranceFTLE: NSTextField!
    @IBOutlet weak var txfFTLEFilter: NSTextField!
    
    // conform tab objects
    @IBOutlet weak var txfFilePathConform: NSTextField!
    @IBOutlet weak var txfLatTolerance: NSTextField!
    @IBOutlet weak var txfLonTolerance: NSTextField!
    @IBOutlet weak var txfDepthTolerance: NSTextField!
    @IBOutlet weak var txfTemporalTolerance: NSTextField!
    

    @IBOutlet weak var mapView: MKMapView!
    @IBOutlet var acCatalog: NSArrayController!
    @IBOutlet weak var tokenField: NSTokenField!
    
    @IBOutlet weak var scMapTypeControl: NSSegmentedControl!
    
    
    
    
    // MARK: - actions
    @IBAction func stopProc(_ sender: Any) {
        if isRunning {
            proc.terminate()
        }
    }

    @IBAction func plotTimeSeries(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            return
        }
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotTS.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }
    
    @IBAction func plotRegionalMap(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            return
        }
        
        let delta = updateQueryParams()
        let pass = sanityCheck_RegionalMap(delta: delta)
        if pass {
            spnBusy.startAnimation(self)
            runScript([pythonPath, "\(opediaAPI)plotRegional.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
            //print(pythonPath, "\(opediaAPI)plotRegional.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, invertLon)
        }
    }

    @IBAction func plotMutualTrend(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 2 {
            _ = Initializer().msgDialog(headline: "Please pick at least two variables!", text: "")
            return
        }
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotXY.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }


    @IBAction func plotHist(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            return
        }
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotDist.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }
    

    @IBAction func plotDepthProfile(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            return
        }
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotDepthProfile.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }

    
    @IBAction func plotSection(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            return
        }
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotSection.py", tables, vars, date1, date2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportFlag, bundlePath])
    }

    
    @IBAction func btnCruiseTrack(_ sender: Any) {
        plotCruise(shapeFlag: "1", colocalizeFlag: "0")
    }
    
    
    @IBAction func btnCruiseColocalize(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            
        } else {
            plotCruise(shapeFlag: "1", colocalizeFlag: "1")
        }
     }
    
    
    @IBAction func swtCruiseMode(_ sender: Any) {

        let virtual = swtCruise.isOn
        txfVirtualCruise.isEnabled = virtual
        btnVirtualCruise.isEnabled = virtual
        pupRegisteredCruise.isEnabled = !virtual
    }
    
    
    @IBAction func btnVirtualCruisePath(_ sender: Any) {
        let opFilePicker: NSOpenPanel = NSOpenPanel()
        opFilePicker.directoryURL = NSURL(fileURLWithPath: bundlePath) as URL
        opFilePicker.allowsMultipleSelection = false
        opFilePicker.canChooseFiles = true
        opFilePicker.canChooseDirectories = false
        opFilePicker.allowedFileTypes = ["csv"]
        opFilePicker.runModal()
        let file = opFilePicker.url
        if (file != nil) { txfVirtualCruise.stringValue = (file?.path)! }
        }
    
    
    @IBAction func btnLagrangianTrack(_ sender: Any) {
        plotLagrangian(shapeFlag: "1", colocalizeFlag: "0")
    }
    
    
    @IBAction func btnLagrangianColocalize(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            
        } else {
            plotLagrangian(shapeFlag: "1", colocalizeFlag: "1")
        }
    }
    
    
    
    @IBAction func btnEddyTrack(_ sender: Any) {
        plotEddy(shapeFlag: "1", colocalizeFlag: "0")
    }

    
    @IBAction func btnEddyColocalize(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            
        } else {
            plotEddy(shapeFlag: "1", colocalizeFlag: "1")
        }
    }
    
    
    @IBAction func btnFTLETrack(_ sender: Any) {
        plotFTLE(shapeFlag: "1", colocalizeFlag: "0")
    }
    
    
    @IBAction func btnFTLEColocalize(_ sender: Any) {
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            
        } else {
            plotFTLE(shapeFlag: "1", colocalizeFlag: "1")
        }
    }
    

    @IBAction func btnFilePathConform(_ sender: Any) {
        let opFilePicker: NSOpenPanel = NSOpenPanel()
        opFilePicker.directoryURL = NSURL(fileURLWithPath: bundlePath) as URL
        opFilePicker.allowsMultipleSelection = false
        opFilePicker.canChooseFiles = true
        opFilePicker.canChooseDirectories = false
        opFilePicker.allowedFileTypes = ["csv", "xlsx"]
        opFilePicker.runModal()
        let file = opFilePicker.url
        if (file != nil) { txfFilePathConform.stringValue = (file?.path)! }
    }

    
    @IBAction func btnDatasetConform(_ sender: Any) {
        
        if (tokenField.objectValue as! NSArray).count < 1 {
            _ = Initializer().msgDialog(headline: "Please pick at least one variable!", text: "")
            return
        }
        
        if (txfFilePathConform.stringValue.count < 1) {
            _ = Initializer().msgDialog(headline: "Please select your data set file.", text: "")
            return
        }
        
        
        let DB = "0"
        let source = txfFilePathConform.stringValue
        let temporalTolerance = txfTemporalTolerance.stringValue
        let latTolerance = txfLatTolerance.stringValue
        let lonTolerance = txfLonTolerance.stringValue
        let depthTolerance = txfDepthTolerance.stringValue

        let extention = NSURL(fileURLWithPath: source).pathExtension! as String
        let pathPrefix = NSURL(fileURLWithPath: source).deletingPathExtension?.path
        let exportPath = pathPrefix! + "_loaded." + ".csv" //+ extention
        
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)colocalize.py", DB, source, temporalTolerance, latTolerance, lonTolerance, depthTolerance, tables, vars, exportPath, bundlePath])
    }
    
    
    @IBAction func scMapType(_ sender: Any) {
        let ind = scMapTypeControl.indexOfSelectedItem
        switch ind {
        case 0:
            mapView.mapType = .standard
        case 1:
            mapView.mapType = .hybrid
        case 2:
            mapView.mapType = .hybridFlyover
        default:
            mapView.mapType = .hybridFlyover
        }
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    func plotFTLE(shapeFlag:String, colocalizeFlag:String) {
        let ftleTable = "tblLCS_REP"
        let ftleValue = txfFTLEFilter.stringValue
        let spatialTolerance = txfSpatialToleranceFTLE.stringValue
        var fteField = "ftle_fw_sla"
        if swtFTLEType.isOn {fteField = "ftle_fw_sla"} else {fteField = "ftle_bw_sla"}
        var bkgComparison = "0"
        if swtFTLEBackgroud.isOn {bkgComparison = "1"} else {bkgComparison = "0"}
        
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)ftle.py", ftleTable, fteField, ftleValue, bkgComparison, date1, date2, lat1, lat2, lon1, lon2, shapeFlag, colocalizeFlag, fname, tables, vars, spatialTolerance, exportFlag, bundlePath])
    }

    
    
    func plotEddy(shapeFlag:String, colocalizeFlag:String) {
        let eddyTable = "tblChelton"
        let spatialTolerance = txfSpatialToleranceEddy.stringValue
        
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)eddy.py", eddyTable, date1, date2, lat1, lat2, lon1, lon2, shapeFlag, colocalizeFlag, fname, tables, vars, spatialTolerance, exportFlag, bundlePath])
    }
    
    
    func plotLagrangian(shapeFlag:String, colocalizeFlag:String) {
        let dt = "\(3600*24)"
        var direction = "1"
        if swtTracer.isOn {
            direction = "1"
        } else {
            direction = "-1"
        }
        let spatialTolerance = txtSpatialToleranceTracer.stringValue
        
        
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)Lagrangian.py", dt, direction, date1, date2, lat1, lon1, shapeFlag, colocalizeFlag, fname, tables, vars, spatialTolerance, exportFlag, bundlePath])
    }
    
    
    func plotCruise(shapeFlag:String, colocalizeFlag:String) {
        var cruiseDB = "1"
        var source = "tblSeaFlow"
        var cruise = pupRegisteredCruise.title
        if swtCruise.isOn {
            cruiseDB="1"
            source = "tblSeaFlow"
            cruise = pupRegisteredCruise.title
        } else {
            cruiseDB="0"
            source = txfVirtualCruise.stringValue
            cruise = (source as NSString).lastPathComponent
        }
        let Resample = pupSamplingRate.title
        let spatialTolerance = txfSpatialToleranceCruise.stringValue
        
        
        spnBusy.startAnimation(self)
        updateQueryParams()
        runScript([pythonPath, "\(opediaAPI)plotCruise.py", cruiseDB, source, cruise, Resample, shapeFlag, colocalizeFlag, fname, tables, vars, spatialTolerance, exportFlag, bundlePath])
        
    }

    
    
    
    func removeAnnotsOverlays() {
        self.mapView.removeAnnotations(self.mapView.annotations)
        self.mapView.removeOverlays(self.mapView.overlays)
        
        addStationALOHA()
    }
 
    
    func addAnnot(lat:Float, lon:Float, title:String, subtitle:String) {
        let annot = MKPointAnnotation()
        annot.coordinate = CLLocationCoordinate2D(latitude: CLLocationDegrees(lat), longitude: CLLocationDegrees(lon))
        if !title.isEmpty { annot.title = title }
        if !subtitle.isEmpty { annot.subtitle = subtitle }
        mapView.addAnnotation(annot)
        mapView.add(MKCircle(center: annot.coordinate, radius: 14000))
        
    }

    
    func addPinAnnot(lat:Float, lon:Float, title:String, subtitle:String) {
        let annot = MKPointAnnotation()
        annot.coordinate = CLLocationCoordinate2D(latitude: CLLocationDegrees(lat), longitude: CLLocationDegrees(lon))
        if !title.isEmpty { annot.title = title }
        if !subtitle.isEmpty { annot.subtitle = subtitle }
        mapView.addAnnotation(annot)
    }

    
    func addStationALOHA(){
        // Adding a pin representing the Station ALOHA
        // addPinAnnot(lat:22.75, lon:-158, title:"Station ALOHA", subtitle:"")
    }
    
    
    func addTrack(_ track: [CLLocationCoordinate2D]) {
        let rad = CLLocationDistance(14000)
        for item in track {
            mapView.add(MKCircle(center: item, radius: rad))
        }
    }
    
    func mapView(_ mapView: MKMapView, rendererFor overlay: MKOverlay) -> MKOverlayRenderer {
        if overlay is MKCircle {
            var circleRenderer = MKCircleRenderer(circle: overlay as! MKCircle)
            circleRenderer.lineWidth = 1.0
            circleRenderer.strokeColor = NSColor(red: 1, green:0.1, blue:0.1, alpha: 1)
            circleRenderer.fillColor = NSColor(red: 1, green:0.1, blue:0.1, alpha: 1)
            circleRenderer.alpha = 0.6
            return circleRenderer
        }
        return MKOverlayRenderer()
    }
    
    func initUI() {
        swtExport.isOn = false
        swtExport.reloadLayer()
        scMapTypeControl.selectedSegment = 2
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

        swtFTLEBackgroud.isOn = false
        swtFTLEBackgroud.reloadLayer()
        
        addStationALOHA()
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
                    if arguments[1].contains("getCatalog") { _ = self.loadCatalog() }
                    if (arguments[1].contains("plotCruise")) ||
                        (arguments[1].contains("Lagrangian")) ||
                        (arguments[1].contains("eddy")) ||
                        (arguments[1].contains("ftle"))
                        { _ = self.loadTrack() }
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
    
    
    func deltas() -> delatParams {
        let deltaDays = Calendar.current.dateComponents([.day], from: dpcStartDate.dateValue, to: dpcEndDate.dateValue).day! + 1
        let deltaLat = dslLat.end - dslLat.start
        let deltaLon = dslLon.end - dslLon.start
        let deltaDepth = Double(pupEndDepth.title)! - Double(pupStartDepth.title)!
        let deltaDepthIndex = pupEndDepth.indexOfSelectedItem - pupStartDepth.indexOfSelectedItem + 1
        return delatParams(days: deltaDays, lats: deltaLat, lons: deltaLon, depths: deltaDepth, depthIndexes: deltaDepthIndex)
    }
    
    func updateQueryParams() -> delatParams {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"        
        (vars, tables, extV1, extVV1, extV2, extVV2) = parseTokens()
        date1 = formatter.string(from: dpcStartDate.dateValue)
        date2 = formatter.string(from: dpcEndDate.dateValue)
        lat1 = "\(dslLat.start)"
        lat2 = "\(dslLat.end)"
        lon1 = "\(dslLon.start)"
        lon2 = "\(dslLon.end)"
        //depth1 = "\(dslDepth.start)"
        //depth2 = "\(dslDepth.end)"
        depth1 = "\(pupStartDepth.title)"
        depth2 = "\(pupEndDepth.title)"
        fname = "figure"
        if swtExport.isOn {
            exportFlag = "1"
        } else {
            exportFlag = "0"
        }
        exportFormat = "csv"
        
        if crossed180 {
            invertLon = "1"
        } else {
            invertLon = "0"
        }
        
        return deltas()
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
            crossed180 = false
            startCoord = coordinates
            startRegionSelect(location)
        case .changed:
            setSpatialControls(startCoord, coordinates)
            drawRect(location)
        case .ended:
            endCoord = coordinates
            if (startCoord.longitude * endCoord.longitude < 0) { crossed180 = true }
            setSpatialControls(startCoord, endCoord)
            endRegionSelect()
        default:
            endRegionSelect()
        }
    }

    
    func loadTrack()-> CSVReader {
        var track = [CLLocationCoordinate2D]()
        removeAnnotsOverlays()
        //https://github.com/yaslab/CSV.swift
        let file = bundlePath + "/shape/shape.csv"
        let stream = InputStream(fileAtPath: file)!
        let csv = try! CSVReader(stream: stream, hasHeaderRow: true)
        //let header = csv.headerRow
       
        var lat: Double = -999
        var lon: Double = -999
        track.removeAll()
        while let row = csv.next() {
            lat = Double(row[0])!
            lon = Double(row[1])!
            track.append( CLLocationCoordinate2D(latitude: CLLocationDegrees(lat), longitude: CLLocationDegrees(lon)) )
        }
        
        addTrack(track)
        return csv
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
        import os
        import site
        file = open("out.txt","w")
        #path = site.getsitepackages()[-1]
        #file.write(path + "/opedia/")
        for pack in site.getsitepackages():
            path = pack + "/opedia/"
            if os.path.isdir(path):
                file.write(path)
                break
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
    

    
    func sanityCheck_RegionalMap(delta: delatParams) -> Bool {
        var res = true
        let vars = (tokenField.objectValue as! NSArray).count
        let plotNumbers = vars * delta.days * delta.depthIndexes
        if plotNumbers > plotCountWarning {
            res = Initializer().msgDialog(headline: "Warning", text: "You've picked:\n\t\t\t\(vars) variable(s)\n\t\t\t\(delta.depthIndexes) depth level(s)\n\t\t\t\(delta.days)-day time period.\n\nYour query may result in large number of plots.\nDo you want to continue?")
        }
        return res
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

