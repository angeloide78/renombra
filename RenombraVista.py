# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class VentanaPrincipal
###########################################################################

class VentanaPrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Renombra v1.0", pos = wx.DefaultPosition, size = wx.Size( 499,613 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerPrincipal = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, u".", u"Selecciona una carpeta", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer2.Add( self.m_dirPicker, 1, wx.ALL, 5 )


		bSizerPrincipal.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_listCtrl_ficheros = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
		bSizer4.Add( self.m_listCtrl_ficheros, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerPrincipal.Add( bSizer4, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Ficheros a cambiar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer9.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizerPrincipal.Add( bSizer9, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Con extensión", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALIGN_CENTER, 5 )

		self.m_textCtrl_ext = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl_ext, 0, wx.ALL, 5 )


		bSizerPrincipal.Add( bSizer5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Renombrar ficheros con", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer13.Add( self.m_staticText7, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizerPrincipal.Add( bSizer13, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Prefijo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetToolTip( u"PRefijo de ficheros" )

		bSizer6.Add( self.m_staticText1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_prefijo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_prefijo, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer6, 1, wx.ALIGN_CENTER, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Sufijo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetToolTip( u"Índice de sufijo de fichero por el que empezará a renombrar" )

		bSizer7.Add( self.m_staticText2, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_sufijo = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer7.Add( self.m_sufijo, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer7, 1, wx.ALIGN_CENTER, 5 )


		bSizerPrincipal.Add( bSizer3, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_button_renombrar = wx.Button( self, wx.ID_ANY, u"Renombrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button_renombrar, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizerPrincipal.Add( bSizer8, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizerPrincipal )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnDirectorioCambiado )
		self.m_button_renombrar.Bind( wx.EVT_BUTTON, self.OnRenombrar )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnDirectorioCambiado( self, event ):
		event.Skip()

	def OnRenombrar( self, event ):
		event.Skip()


