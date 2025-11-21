from PIL import Image, ImageCms

img = Image.open('soleil.jpg')

# Available via https://www.adobe.com/support/downloads/iccprofiles/iccprofiles_win.html
fp = 'icc/icc/'
rgb_icc = fp+"RGB/" + 'AppleRGB.icc'
cmyk_icc = fp+"CMYK/"+"WebCoatedSWOP2006Grade5.icc"

im = ImageCms.profileToProfile(img, rgb_icc, cmyk_icc, renderingIntent=0, outputMode='CMYK')
source = im.split()

# create blank image and split the layers
blank = Image.new("CMYK", im.size, (0,0,0,0))
b_split = blank.split()

# add the separate layers to the k layer
c_out = Image.merge("CMYK",(b_split[0], b_split[1], b_split[2], source[0]))
m_out = Image.merge("CMYK",(b_split[0], b_split[1], b_split[2], source[1]))
y_out = Image.merge("CMYK",(b_split[0], b_split[1], b_split[2], source[2]))
k_out = Image.merge("CMYK",(b_split[0], b_split[1], b_split[2], source[3]))

out = Image.merge("CMYK",(source[0],  source[1], source[2], source[3]))

# Colour versions

c_out_rgb = ImageCms.profileToProfile(c_out, cmyk_icc, rgb_icc, renderingIntent=0, outputMode='RGB')
c_out_rgb.save('f_c.png','PNG',optimize=False)

m_out_rgb = ImageCms.profileToProfile(m_out, cmyk_icc, rgb_icc, renderingIntent=0, outputMode='RGB')
m_out_rgb.save('f_m.png','PNG',optimize=False)

y_out_rgb = ImageCms.profileToProfile(y_out, cmyk_icc, rgb_icc, renderingIntent=0, outputMode='RGB')
y_out_rgb.save('f_y.png','PNG',optimize=False)

k_out_rgb = ImageCms.profileToProfile(k_out, cmyk_icc, rgb_icc, renderingIntent=0, outputMode='RGB')
k_out_rgb.save('f_k.png','PNG',optimize=False)

out_rgb = ImageCms.profileToProfile(out, cmyk_icc, rgb_icc, renderingIntent=0, outputMode='RGB')
out_rgb.save('out.png','PNG',optimize=False)
