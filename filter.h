
class Filter
{
public:

  std::string GetName() const;

  std::string ToString() const;

  Self &SetParameter(double pixelValue);
  double GetParameter() const;

  Self &SetDimensionParameter(std::vector<unsigned int> dimValue);
  std::vector<unsigned int> GetDimensionParaeter() const;

  double GetMeasurement() const;

  Image Execute(const Image &image1);
  Image Execute( onst Image &image1, double pixelValue, std::vector<unsigned int> dimValue);

};

Image Filter(const Image &image1, double pixelValue = 0, std::vector<unsigned int> dimValue = defaultValue);
