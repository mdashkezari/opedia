//
//  CatalogVar.swift
//  opedia
//
//  Created by Mohammad Dehghani Ashkezari on 2018-08-19.
//  Copyright © 2018 Mohammad Dehghani Ashkezari. All rights reserved.
//

import Foundation


class CatalogVar: NSObject {
    @objc var short_name: String
    @objc var long_name: String
    @objc var unit: String
    @objc var make: String
    @objc var sensor: String
    @objc var process_level: String
    @objc var study_domain: String
    @objc var temporal_resolution: String
    @objc var spatial_resolution: String
    @objc var dataset_name: String
    @objc var data_source: String
    @objc var distributor: String
    @objc var id: String
    @objc var table_name: String
    @objc var keywords: String
    
    init(short_name: String, long_name: String, unit: String, make: String, sensor: String, process_level: String, study_domain: String, temporal_resolution: String, spatial_resolution: String, dataset_name: String, data_source: String, distributor: String, id: String, table_name: String, keywords: String) {
        self.short_name = short_name
        self.long_name = long_name
        self.unit = unit
        self.make = make
        self.sensor = sensor
        self.process_level = process_level
        self.study_domain = study_domain
        self.temporal_resolution = temporal_resolution
        self.spatial_resolution = spatial_resolution
        self.dataset_name = dataset_name
        self.data_source = data_source
        self.distributor = distributor
        self.id = id
        self.table_name = table_name
        self.keywords = keywords
    }
}
