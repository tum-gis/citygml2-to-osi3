-- View: osi.genericattribs

-- DROP MATERIALIZED VIEW osi.genericattribs;

CREATE MATERIALIZED VIEW IF NOT EXISTS osi.genericattribs
TABLESPACE pg_default
AS
 SELECT cityobject_genericattrib.cityobject_id,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'geometry_rotation_x'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS geometry_rotation_x,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'geometry_rotation_y'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS geometry_rotation_y,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'geometry_rotation_z'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS geometry_rotation_z,
    (array_agg(cityobject_genericattrib.intval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_laneId'::text) AND (cityobject_genericattrib.intval IS NOT NULL))))[1] AS "identifier_laneId",
    (array_agg(cityobject_genericattrib.intval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_laneSectionId'::text) AND (cityobject_genericattrib.intval IS NOT NULL))))[1] AS "identifier_laneSectionId",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_modelDate'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_modelDate",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_modelName'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_modelName",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_modelVendor'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_modelVendor",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_roadId'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_roadId",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_roadObjectId'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_roadObjectId",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_roadObjectName'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_roadObjectName",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_sourceFileExtension'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_sourceFileExtension",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_sourceFileHashSha256'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_sourceFileHashSha256",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_sourceFileName'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_sourceFileName",
    (array_agg(cityobject_genericattrib.intval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_laneId'::text) AND (cityobject_genericattrib.intval IS NOT NULL))))[1] AS "identifier_to_laneId",
    (array_agg(cityobject_genericattrib.intval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_laneSectionId'::text) AND (cityobject_genericattrib.intval IS NOT NULL))))[1] AS "identifier_to_laneSectionId",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_modelDate'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_to_modelDate",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_modelName'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_to_modelName",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_modelVendor'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_to_modelVendor",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_roadId'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_to_roadId",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_sourceFileExtension'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_to_sourceFileExtension",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_sourceFileHashSha256'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_to_sourceFileHashSha256",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'identifier_to_sourceFileName'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "identifier_to_sourceFileName",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_heightOffset_curvePositionStart_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_heightOffset_curvePositionStart_0",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_heightOffset_curvePositionStart_1'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_heightOffset_curvePositionStart_1",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_heightOffset_inner_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_heightOffset_inner_0",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_heightOffset_inner_1'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_heightOffset_inner_1",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_heightOffset_outer_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_heightOffset_outer_0",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_heightOffset_outer_1'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_heightOffset_outer_1",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_level'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_lane_level,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_material_curvePositionStart_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_material_curvePositionStart_0",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_material_friction_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS opendrive_lane_material_friction_0,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_material_roughness_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS opendrive_lane_material_roughness_0,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_material_surface_0'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_lane_material_surface_0,
    (array_agg(cityobject_genericattrib.intval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_predecessor_lane_0'::text) AND (cityobject_genericattrib.intval IS NOT NULL))))[1] AS opendrive_lane_predecessor_lane_0,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_laneSection_curvePositionStart'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_laneSection_curvePositionStart",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_speed_curvePositionStart_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_lane_speed_curvePositionStart_0",
    (array_agg(cityobject_genericattrib.unit) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_speed_max_0_unit'::text) AND (cityobject_genericattrib.unit IS NOT NULL))))[1] AS opendrive_lane_speed_max_0_unit,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_speed_max_0'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS opendrive_lane_speed_max_0,
    (array_agg(cityobject_genericattrib.intval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_successor_lane_0'::text) AND (cityobject_genericattrib.intval IS NOT NULL))))[1] AS opendrive_lane_successor_lane_0,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_lane_type'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_lane_type,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_junction'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_road_junction,
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_length'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS opendrive_road_length,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadMarking_color'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadMarking_color",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadMarking_curvePositionStart'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_roadMarking_curvePositionStart",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadMarking_material'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadMarking_material",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadMarking_type'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadMarking_type",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadMarking_weight'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadMarking_weight",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadMarking_width'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_roadMarking_width",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadObject_dynamic'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadObject_dynamic",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadObject_orientation'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadObject_orientation",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadObject_type'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadObject_type",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadObject_validLength'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_roadObject_validLength",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_predecessor_contactPoint'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_road_predecessor_contactPoint",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_predecessor_junction'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_road_predecessor_junction,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_predecessor_road'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_road_predecessor_road,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_rule'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_road_rule,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadSignal_countryCode'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadSignal_countryCode",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadSignal_dynamic'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadSignal_dynamic",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadSignal_orientation'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadSignal_orientation",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadSignal_subtype'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadSignal_subtype",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadSignal_type'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_roadSignal_type",
    (array_agg(cityobject_genericattrib.realval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_roadSignal_value'::text) AND (cityobject_genericattrib.realval IS NOT NULL))))[1] AS "opendrive_roadSignal_value",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_successor_contactPoint'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS "opendrive_road_successor_contactPoint",
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_successor_junction'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_road_successor_junction,
    (array_agg(cityobject_genericattrib.strval) FILTER (WHERE (((cityobject_genericattrib.attrname)::text = 'opendrive_road_successor_road'::text) AND (cityobject_genericattrib.strval IS NOT NULL))))[1] AS opendrive_road_successor_road
   FROM cityobject_genericattrib
  GROUP BY cityobject_genericattrib.cityobject_id
WITH DATA;

ALTER TABLE osi.genericattribs
    OWNER TO postgres;

-- View: osi.TrafficSign

-- DROP MATERIALIZED VIEW osi.TrafficSign;

CREATE MATERIALIZED VIEW IF NOT EXISTS osi.TrafficSign
TABLESPACE pg_default
AS
 SELECT ga.cityobject_id,
    ga.geometry_rotation_x,
    ga.geometry_rotation_y,
    ga.geometry_rotation_z,
    ga."identifier_roadObjectName",
    ga."identifier_roadObjectId",
    ga."opendrive_roadSignal_countryCode",
    ga."opendrive_roadSignal_type",
    ga."opendrive_roadSignal_subtype",
    ga."opendrive_roadSignal_value",
    st_x(cf.lod1_other_geom) AS centroid_x,
    st_y(cf.lod1_other_geom) AS centroid_y,
    st_z(cf.lod1_other_geom) AS centroid_z,
    cf.lod1_other_geom AS geom
   FROM ((osi."genericattribs" ga
     LEFT JOIN surface_geometry sg ON ((sg.cityobject_id = ga.cityobject_id)))
     LEFT JOIN city_furniture cf ON ((cf.id = ga.cityobject_id)))
  WHERE ((ga."identifier_roadObjectName")::text = ANY (ARRAY[('Gefahrzeichen'::character varying)::text, ('Richtzeichen'::character varying)::text, ('Verkehrseinrichtungen'::character varying)::text, ('Vorschriftzeichen'::character varying)::text, ('ZUSATZZEICHEN'::character varying)::text]))
WITH DATA;

ALTER TABLE osi.TrafficSign
    OWNER TO postgres;


-- View: osi.StationaryObject

-- DROP MATERIALIZED VIEW osi."StationaryObject";

CREATE MATERIALIZED VIEW IF NOT EXISTS osi."StationaryObject"
TABLESPACE pg_default
AS
 SELECT ga.cityobject_id,
    ga."opendrive_roadObject_type" AS "Type",
    st_force2d(st_convexhull(st_collect(sg.geometry))) AS basepolygon,
    ga.geometry_rotation_x,
    ga.geometry_rotation_y,
    ga.geometry_rotation_z,
    (st_xmax((st_collect(sg.geometry))::box3d) - st_xmin((st_collect(sg.geometry))::box3d)) AS width,
    (st_ymax((st_collect(sg.geometry))::box3d) - st_ymin((st_collect(sg.geometry))::box3d)) AS length,
    (st_zmax((st_collect(sg.geometry))::box3d) - st_zmin((st_collect(sg.geometry))::box3d)) AS height,
    st_x(st_centroid(st_collect(sg.geometry))) AS centroid_x,
    st_y(st_centroid(st_collect(sg.geometry))) AS centroid_y,
    (((st_zmax((st_collect(sg.geometry))::box3d) - st_zmin((st_collect(sg.geometry))::box3d)) / (2)::double precision) + st_zmin((st_collect(sg.geometry))::box3d)) AS centroid_z,
    ga."identifier_modelName" AS model_reference
   FROM (osi."genericattribs" ga
     JOIN surface_geometry sg ON ((ga.cityobject_id = sg.cityobject_id)))
  WHERE ((ga."opendrive_roadObject_type" IS NOT NULL) AND ((ga."opendrive_roadObject_type")::text <> 'NONE'::text))
  GROUP BY ga.cityobject_id, ga."opendrive_roadObject_type", ga.geometry_rotation_x, ga.geometry_rotation_y, ga.geometry_rotation_z, ga."identifier_modelName"
WITH DATA;

ALTER TABLE osi."StationaryObject"
    OWNER TO postgres;


-- View: osi.RoadMarking

-- DROP MATERIALIZED VIEW osi."RoadMarking";

CREATE MATERIALIZED VIEW IF NOT EXISTS osi."RoadMarking"
TABLESPACE pg_default
AS
 SELECT ga.cityobject_id
    , ga."identifier_roadId"
    , ga."identifier_laneSectionId"
    , ga."identifier_laneId"
    , gco.lod2_other_geom AS geom
    , ga."opendrive_roadMarking_color"
    , ga."opendrive_roadMarking_curvePositionStart"
    , ga."opendrive_roadMarking_material"
    , ga."opendrive_roadMarking_type"
    , ga."opendrive_roadMarking_weight"
    , ga."opendrive_roadMarking_width"
  FROM osi.genericattribs AS ga
  INNER JOIN citydb.generic_cityobject AS gco ON gco.id = ga.cityobject_id
  INNER JOIN cityobject AS co ON co.id = ga.cityobject_id
  WHERE co.name = 'RoadMarking'
WITH DATA;

ALTER TABLE osi."RoadMarking"
    OWNER TO postgres;


-- View: osi.LaneBoundary

-- DROP MATERIALIZED VIEW osi."LaneBoundary";

CREATE MATERIALIZED VIEW IF NOT EXISTS osi."LaneBoundary"
TABLESPACE pg_default
AS
  SELECT --gco.id
    co.id
    , (CASE WHEN co.name = 'LeftLaneBoundary' THEN 'LEFT' ELSE 'RIGHT' END) AS side
    , gco.lod2_other_geom AS geom
    , ga."identifier_laneId"
    , ga."identifier_laneSectionId"
    , ga."identifier_roadId"
    , rm."opendrive_roadMarking_color"
    , rm."opendrive_roadMarking_material"
    , rm."opendrive_roadMarking_type"
    , rm."opendrive_roadMarking_width"
    , rm."opendrive_roadMarking_weight"
  FROM citydb.generic_cityobject AS gco
  INNER JOIN citydb.cityobject AS co ON co.id= gco.id
  INNER JOIN osi."genericattribs" AS ga ON ga.cityobject_id = gco.id
  LEFT JOIN osi."RoadMarking" AS rm ON rm."identifier_roadId" = ga."identifier_roadId" AND rm."identifier_laneId" = ga."identifier_laneId" AND rm."identifier_laneSectionId" = ga."identifier_laneSectionId" AND rm."geom" = gco."lod2_other_geom"
  WHERE co.name IN ('RightLaneBoundary', 'LeftLaneBoundary')
 WITH DATA;

ALTER TABLE osi."LaneBoundary"
    OWNER TO postgres;


-- View: osi.Lane

-- DROP MATERIALIZED VIEW osi."Lane";

CREATE MATERIALIZED VIEW IF NOT EXISTS osi."Lane"
TABLESPACE pg_default
AS
  SELECT --gco.id
    co.id
    , co.name
    , gco.lod2_other_geom AS geom
    , rlb.id AS "right_lane_boundary_id"
    , llb.id AS "left_lane_boundary_id"
    , ga."identifier_laneId"
    , ga."identifier_laneSectionId"
    , ga."identifier_roadId"
    , ls."opendrive_lane_type"
    , ls."opendrive_road_junction"
    , ls."opendrive_road_predecessor_junction"
    , ls."opendrive_road_successor_junction"    
    , ls."opendrive_road_predecessor_road"
    , ls."opendrive_road_successor_road"
  FROM citydb.generic_cityobject AS gco
  INNER JOIN citydb.cityobject AS co ON co.id= gco.id
  INNER JOIN osi.genericattribs AS ga ON ga.cityobject_id = gco.id
  INNER JOIN (
    SELECT "identifier_roadId"
      , "identifier_laneSectionId"
      , "identifier_laneId"
      , "opendrive_lane_type"
      , "opendrive_road_junction"
      , "opendrive_road_predecessor_junction"
      , "opendrive_road_successor_junction"
      , "opendrive_road_predecessor_road"
      , "opendrive_road_successor_road"
      , "opendrive_lane_heightOffset_curvePositionStart_0"
      , "opendrive_lane_heightOffset_curvePositionStart_1"
      , "opendrive_lane_heightOffset_inner_0"
      , "opendrive_lane_heightOffset_inner_1"
      , "opendrive_lane_heightOffset_outer_0"
      , "opendrive_lane_heightOffset_outer_1"
      , "opendrive_lane_level"
      , "opendrive_lane_material_curvePositionStart_0"
      , "opendrive_lane_material_friction_0"
      , "opendrive_lane_material_roughness_0"
      , "opendrive_lane_material_surface_0"
      , "opendrive_lane_predecessor_lane_0"
      , "opendrive_laneSection_curvePositionStart"
      , "opendrive_lane_speed_curvePositionStart_0"
      , "opendrive_lane_speed_max_0"
      , "opendrive_lane_successor_lane_0"
      , "opendrive_road_predecessor_contactPoint"
      , "opendrive_road_length"
      FROM osi."genericattribs" INNER JOIN cityobject ON id = cityobject_id WHERE name = 'LaneSurface'
  ) AS ls ON ls."identifier_roadId" = ga."identifier_roadId" AND ls."identifier_laneId" = ga."identifier_laneId" AND ls."identifier_laneSectionId" = ga."identifier_laneSectionId"
  INNER JOIN (
    SELECT * FROM osi."LaneBoundary" WHERE side = 'LEFT'
  ) AS llb ON llb."identifier_roadId" = ga."identifier_roadId" AND llb."identifier_laneId" = ga."identifier_laneId" AND llb."identifier_laneSectionId" = ga."identifier_laneSectionId"
  INNER JOIN (
    SELECT * FROM osi."LaneBoundary" WHERE side = 'RIGHT'
  ) AS rlb ON rlb."identifier_roadId" = ga."identifier_roadId" AND rlb."identifier_laneId" = ga."identifier_laneId" AND rlb."identifier_laneSectionId" = ga."identifier_laneSectionId"
  WHERE co.name = 'LaneCenterLine'
 WITH DATA;

ALTER TABLE osi."Lane"
    OWNER TO postgres;