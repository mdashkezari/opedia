function otile(nrt, obs, itnums, Xres, Yres)
	addpath('tile/');
	if nrt
		if obs
			TileCMEMS_NRT_SLA(itnums,Xres,Yres);
			TileAVISO_NRT_ADT(itnums,Xres,Yres);
		
			Tile_NRT_Phase_SLA(itnums,Xres,Yres);
			Tile_NRT_Phase_ADT(itnums,Xres,Yres);

			TileAVISO_NRT_Vort_SLA(itnums,Xres,Yres);
                        TileAVISO_NRT_Vort_ADT(itnums,Xres,Yres);

                        TileMODIS_NRT_CHL(itnums);
                        TileMURSST_NRT_SST(itnums);
		else

		end
	else
                if obs 
			TileCMEMS_REP_SLA(itnums,Xres,Yres);
			TileAVISO_REP_ADT(itnums,Xres,Yres);

			Tile_REP_Phase_SLA(itnums,Xres,Yres);
			Tile_REP_Phase_ADT(itnums,Xres,Yres);

                        TileAVISO_REP_Vort_SLA(itnums,Xres,Yres);
                        TileAVISO_REP_Vort_ADT(itnums,Xres,Yres);
                else

                end
	end

end
