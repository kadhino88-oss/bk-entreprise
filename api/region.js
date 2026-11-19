// Renvoie le pays du visiteur (en-tête géographique fourni par Vercel) pour choisir la devise affichée.
// Aucune donnée n'est enregistrée : l'en-tête est lu puis oublié.
module.exports = function handler(req, res) {
  var country = String(req.headers['x-vercel-ip-country'] || '').toUpperCase().slice(0, 2);
  res.setHeader('Cache-Control', 'private, no-store');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.status(200).send(JSON.stringify({ country: /^[A-Z]{2}$/.test(country) ? country : '' }));
};
