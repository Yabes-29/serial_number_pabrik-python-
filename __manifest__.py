{
  'name': 'Serial Number',
  'author': 'Bayu Dwi Saputra & Ibnu Nur Khawarizmi',
  'version': '0.1',
  'depends': [
    'sale','product','mrp','serial_pabrik'
  ],
  'data': [
    
    'views/mrp_serial_number.xml',
    'report/report_mrp_serial_number.xml', 
    'data/mrp_serial_number_sequence.xml'
    
  ],

  'qweb': [

  ],
  'sequence': 4,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': 'Serial Number',
  'summary': 'Serial Number for After Sales PT.Innovasi Sarana Grafindo',
  'license': 'OPL-1',
  'images': ['static/description/icon.png'],
  'description': '-'
}
