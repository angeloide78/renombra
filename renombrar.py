import wx
import os

from RenombraVista import VentanaPrincipal

class Ventana(VentanaPrincipal):

  def __init__(self, parent):
    VentanaPrincipal.__init__(self, parent)
    self.m_listCtrl_ficheros.InsertColumn(0, 'Ficheros',width=1000)
    self.directory = '.'
    self.rellenar_lista()
    
  def __cargar_ficheros(self, directory):
    self.m_listCtrl_ficheros.DeleteAllItems()
    for filename in os.listdir(directory):
      if os.path.isdir(os.path.join(directory, filename)):
        index = self.filedir
      else:
        index = self.file
      self.m_listCtrl_ficheros.InsertItem(self.m_listCtrl_ficheros.GetItemCount(), filename, index)
    
  def rellenar_lista(self):
    # directory = '.'
    il = wx.ImageList(16, 16)
    self.m_listCtrl_ficheros.AssignImageList(il, wx.IMAGE_LIST_SMALL)
    self.filedir = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
    self.file = il.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
    self.__cargar_ficheros(self.directory)
  
  def OnDirectorioCambiado( self, event ):
    self.directory = self.m_dirPicker.GetPath()
    self.__cargar_ficheros(self.directory)

  def OnRenombrar( self, event ):
    extension = self.m_textCtrl_ext.GetValue().strip()
    prefijo = self.m_prefijo.GetValue().strip()
    sufijo = int(self.m_sufijo.GetValue())
    
    if len(extension) == 0:
      wx.MessageBox("Es necesario especificar la extensión de los ficheros a renombrar")
    else:
      lista_ficheros = os.listdir(self.directory)
    
      # Recorrer cada archivo en la lista de archivos
      for nfich in lista_ficheros:
        
        # Verificar si el archivo tiene la extensión correcta
        if nfich.endswith(extension):
          
          # Construir el nuevo nombre de archivo
          if len(prefijo) == 0: 
            fichero_nuevo = "{}.{}".format(str(sufijo), extension)
          else:
            fichero_nuevo = "{}_{}.{}".format(prefijo, str(sufijo), extension)

          # Se construye la ruta absoluta con los nombres de fichero nuevo y antiguo.
          fichero_original = os.path.join(self.directory, nfich)
          fichero_nuevo = os.path.join(self.directory, fichero_nuevo)
          
          # Renombrar el archivo
          os.rename(fichero_original, fichero_nuevo)      
          sufijo += 1
      
      # Se vuelve a recargar el directorio actual.
      self.__cargar_ficheros(self.directory)
      
app = wx.App()
ventana = Ventana(None)
ventana.Show()
app.MainLoop()
