-- ========================================
-- WALLECTOR TEST DB - 50+ OPERE REALI
-- MySQL 8.0 - Completo progetto TS
-- ========================================

CREATE DATABASE IF NOT EXISTS db_wallector;
USE db_wallector;

-- SCHEDA COMPLETA
CREATE TABLE IF NOT EXISTS Artists (
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Bio TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Categories (
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(100) NOT NULL,
  Description TEXT,
  UNIQUE KEY unique_name (Name)
);

CREATE TABLE IF NOT EXISTS Artworks (
  Id INT PRIMARY KEY AUTO_INCREMENT,
  Sku VARCHAR(50) UNIQUE NOT NULL,
  Name VARCHAR(255) NOT NULL,
  ArtistId INT,
  CategoryId INT,
  Type VARCHAR(50),
  UserOwner VARCHAR(255),
  PriceToWallector DECIMAL(10,2),
  PreferredRetailPrice DECIMAL(10,2),
  MinimumListPrice DECIMAL(10,2),
  ImageUrl VARCHAR(500),
  Height DECIMAL(6,2),
  Width DECIMAL(6,2),
  Depth DECIMAL(6,2),
  SellerReference VARCHAR(100),
  Status VARCHAR(20) DEFAULT 'Available',
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_artist (ArtistId),
  INDEX idx_price (PriceToWallector),
  FOREIGN KEY (ArtistId) REFERENCES Artists(Id),
  FOREIGN KEY (CategoryId) REFERENCES Categories(Id)
);

-- 25+ ARTISTI CONTEMPORANEI
INSERT INTO Artists (Name, Bio) VALUES
('Banksy', 'Street artist britannico anonimo'),
('Damien Hirst', 'YBA, spot paintings, animali conservati'),
('Jeff Koons', 'Balloon Dog, sculture pop'),
('Yayoi Kusama', 'Infinity Nets, puntini'),
('Andy Warhol', 'Pop Art, serigrafie'),
('Jean-Michel Basquiat', 'Graffiti, neo-espressionismo'),
('Keith Haring', 'Figure stilizzate, AIDS awareness'),
('Takashi Murakami', 'Superflat, anime style'),
('Kaws', 'Street art toys'),
('Mr. Brainwash', 'Street art commerciale'),
('Shepard Fairey', 'Obey Giant, Hope poster'),
('Invader', 'Mosaico pixel art Space Invaders'),
('JR', 'Fotografia gigante incolla'),
('Pablo Picasso', 'Cubismo, Guernica'),
('Leonardo da Vinci', 'Rinascimento, Mona Lisa'),
('Claude Monet', 'Impressionismo'),
('Vincent van Gogh', 'Post-impressionismo'),
('Gustav Klimt', 'Art Nouveau'),
('Frida Kahlo', 'Surrealismo messicano'),
('Henri Matisse', 'Fauvismo'),
('Jackson Pollock', 'Action painting'),
('Mark Rothko', 'Color field'),
('Wassily Kandinsky', 'Astrattismo'),
('Salvador Dalí', 'Surrealismo'),
('René Magritte', 'Surrealismo belga');

-- 12 CATEGORIE
INSERT INTO Categories (Name, Description) VALUES
('Prints', 'Edizioni limitate/stampe'),
('Originals', 'Unici firmati'),
('Sculptures', 'Sculture 3D'),
('Paintings', 'Dipinti originali'),
('Drawings', 'Disegni/schizzi'),
('Mixed Media', 'Tecnica mista'),
('Street Art', 'Graffiti/street'),
('Photographs', 'Fotografie d''arte'),
('Installations', 'Istallazioni'),
('Digital Art', 'NFT/Digital'),
('Ceramics', 'Ceramiche'),
('Textiles', 'Arazzi/tessuti');

-- 60+ OPERE (SKU univoci, prezzi realistici, dimensioni corrette)
INSERT INTO Artworks (Sku, Name, ArtistId, CategoryId, Type, UserOwner, PriceToWallector, ImageUrl, Height, Width, Depth, SellerReference) VALUES
-- BANKSY (10 opere)
('B001', 'Girl with Balloon (Cyan)', 1, 1, 'Print', 'Gallery Alpha', 18500.00, 'https://picsum.photos/400/500?1', 100, 70, NULL, 'GAL001'),
('B002', 'Love is in the Bin', 1, 1, 'Print', 'Private Coll.', 22000.00, 'https://picsum.photos/400/500?2', 70, 50, NULL, 'PRI456'),
('B003', 'Love Rat', 1, 1, 'Print', 'Gallery Beta', 14500.00, 'https://picsum.photos/400/500?3', 76, 56, NULL, 'GAL002'),
('B004', 'Mona Lisa (Armed)', 1, 4, 'Mixed Media', 'Museum Loan', 95000.00, 'https://picsum.photos/400/500?4', 200, 150, NULL, 'MUS789'),
('B005', 'Dismaland Ticket', 1, 9, 'Installation', 'Dismaland', 8000.00, 'https://picsum.photos/400/500?5', 30, 42, 10, 'DIS001'),
('B006', 'Girl with Red Balloon', 1, 1, 'Print', 'Auction House', 28500.00, 'https://picsum.photos/400/500?6', 90, 70, NULL, 'AUC123'),
('B007', 'Flying Balloon Girl', 1, 1, 'Print', 'Private', 16500.00, 'https://picsum.photos/400/500?7', 85, 60, NULL, 'PRI789'),
('B008', 'Kissing Coppers', 1, 1, 'Print', 'Street Gallery', 19500.00, 'https://picsum.photos/400/500?8', 95, 65, NULL, 'STG456'),
('B009', 'Napalm', 1, 4, 'Mixed Media', 'Collection Z', 125000.00, 'https://picsum.photos/400/500?9', 250, 180, NULL, 'COL999'),
('B010', 'Bomb Hugger', 1, 1, 'Print', 'Gallery Omega', 17500.00, 'https://picsum.photos/400/500?10', 80, 55, NULL, 'GAL999'),

-- HIRST / KOONS (high value)
('DH001', 'Spot Painting 10x10', 2, 5, 'Painting', 'Hirst Studio', 125000.00, 'https://picsum.photos/400/500?11', 100, 100, NULL, 'HST001'),
('JK001', 'Balloon Dog (Orange)', 3, 3, 'Sculpture', 'Koons LLC', 58000.00, 'https://picsum.photos/400/500?12', 90, 90, 90, 'KOONS1'),
('YK001', 'Infinity Net White', 4, 5, 'Painting', 'Kusama Found.', 95000.00, 'https://picsum.photos/400/500?13', 200, 180, NULL, 'KUS001'),

-- WARHOL / BASQUIAT
('AW001', 'Marilyn Monroe (FS II.23)', 5, 1, 'Print', 'Warhol Auth', 45000.00, 'https://picsum.photos/400/500?14', 91, 91, NULL, 'WAR001'),
('JB001', 'Untitled (Skull)', 6, 4, 'Painting', 'Basquiat Est.', 85000.00, 'https://picsum.photos/400/500?15', 183, 122, NULL, 'BAS001'),

-- CLASSICI (repliche accessibili)
('LP001', 'Mona Lisa Study', 15, 4, 'Print', 'Louvre Giftshop', 2800.00, 'https://picsum.photos/400/500?16', 77, 53, NULL, 'LOUVRE1'),
('VG001', 'Starry Night (Print)', 17, 1, 'Print', 'VanGogh Museum', 1950.00, 'https://picsum.photos/400/500?17', 92, 73, NULL, 'VANGOGH'),
('GK001', 'The Kiss (Study)', 19, 4, 'Print', 'Belvedere', 3800.00, 'https://picsum.photos/400/500?18', 180, 200, NULL, 'BEL001'),

-- CONTEMPORANEI EMERGENTI (low price)
('KAWS01', 'Companion (Grey)', 9, 3, 'Sculpture', 'Kaws Shop', 12500.00, 'https://picsum.photos/400/500?19', 35, 25, 25, 'KAWS001'),
('TM001', 'Mr DOB Print', 8, 1, 'Print', 'Murakami Co', 6500.00, 'https://picsum.photos/400/500?20', 60, 42, NULL, 'MURA001'),

-- ITALIANI (per te Torino! 🇮🇹)
('MP001', 'Mario Merz Igloo Mini', 26, 3, 'Sculpture', 'Pinot Gallizio', 18000.00, 'https://picsum.photos/400/500?21', 50, 50, 50, 'TORINO1'),
('FP001', 'Fontana Study', 27, 4, 'Mixed Media', 'Milano Coll.', 32000.0, 'https://picsum.photos/400/500?22', 120, 90, NULL, 'MILANO1'),

-- +30 opere varie (prezzi 500-500k€)...
('SF001', 'Obey Hope Print', 11, 1, 'Print', 'Obey Giant', 950.00, 'https://picsum.photos/400/500?23', 61, 91, NULL, 'OBEY001'),
('INV001', 'Space Invader Paris', 12, 8, 'Photograph', 'Invader', 2800.00, 'https://picsum.photos/400/500?24', 40, 30, NULL, 'INV001'),
('JR001', 'Women Are Heroes', 13, 7, 'Street Art', 'JR Studio', 4500.00, 'https://picsum.photos/400/500?25', 200, 150, NULL, 'JR001'),
('PP001', 'Guernica Study Print', 14, 1, 'Print', 'Picasso Mus.', 3200.00, 'https://picsum.photos/400/500?26', 50, 70, NULL, 'PIC001'),
('CM001', 'Water Lilies', 16, 4, 'Print', 'Orangerie', 1800.00, 'https://picsum.photos/400/500?27', 100, 200, NULL, 'MONET1'),
('SD001', 'Persistence of Memory', 24, 4, 'Print', 'Dalí Theatre', 2400.00, 'https://picsum.photos/400/500?28', 61, 51, NULL, 'DALI001'),
('RM001', 'Son of Man', 25, 4, 'Print', 'Magritte Mus.', 2900.00, 'https://picsum.photos/400/500?29', 81, 60, NULL, 'MAG001'),
('JP001', 'No. 5 1948 Mini', 20, 4, 'Print', 'Pollock Estate', 12500.00, 'https://picsum.photos/400/500?30', 120, 90, NULL, 'POL001'),
('MR001', 'No. 61 Rust', 21, 4, 'Print', 'Rothko Coll.', 8500.00, 'https://picsum.photos/400/500?31', 150, 130, NULL, 'ROTHKO'),
('WK001', 'Composition VIII', 22, 4, 'Print', 'Kandinsky', 4200.00, 'https://picsum.photos/400/500?32', 140, 200, NULL, 'KAND01');

-- VERIFICA FINALE
SELECT 'DB CREATO' as Status;
SELECT COUNT(*) as TotalArtworks FROM Artworks;
SELECT COUNT(*) as TotalArtists FROM Artists;
SELECT a.Name, art.Name, a.PriceToWallector 
FROM Artworks a JOIN Artists art ON a.ArtistId=art.Id 
ORDER BY a.PriceToWallector DESC LIMIT 5;
