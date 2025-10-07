#pragma once

#include <vector>
#include <memory>

namespace qynva {

/**
 * @brief Base class for tensor operations
 * 
 * This class provides the foundation for bio-tensor optimization
 * and helical tensor structure implementations.
 */
class Tensor {
public:
    Tensor() = default;
    virtual ~Tensor() = default;
    
    // Copy constructor and assignment
    Tensor(const Tensor&) = default;
    Tensor& operator=(const Tensor&) = default;
    
    // Move constructor and assignment
    Tensor(Tensor&&) = default;
    Tensor& operator=(Tensor&&) = default;
    
    /**
     * @brief Get tensor dimensions
     * @return Vector containing the size of each dimension
     */
    virtual std::vector<size_t> dimensions() const = 0;
    
    /**
     * @brief Get total number of elements in the tensor
     * @return Total element count
     */
    virtual size_t size() const = 0;
};

} // namespace qynva