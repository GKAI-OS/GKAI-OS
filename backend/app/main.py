from fastapi import FastAPI

from app.database import Base, engine

# import models
from app.models import brand
from app.models import category
from app.models import vehicle
from app.models import vehicle_spec
from app.models import vehicle_image
from app.models import vehicle_feature
from app.models import vehicle_variant
from app.models import vehicle_performance
from app.models import vehicle_price
from app.models import vehicle_fuel
from app.models import vehicle_safety
from app.models import vehicle_dimension
from app.models import vehicle_color
from app.models import vehicle_mileage
from app.models import vehicle_review
from app.models import vehicle_faq
from app.models import vehicle_source
from app.models import search_intent
from app.models import vehicle_interest
from app.models import vehicle_recommendation
from app.models import vehicle_comparison
from app.models import vehicle_seo
from app.models import vehicle_trend
from app.models import vehicle_trend_history
from app.models import ai_vehicle_score
from app.models import ai_recommendation
from app.models import user_interaction
from app.models import user_preference
from app.models import module_name
from app.models import vehicle_rating


from app.api.brands import router as brand_router
from app.api.categories import router as category_router
from app.api.vehicles import router as vehicle_router
from app.api.vehicle_spec import router as vehicle_spec_router
from app.api.vehicle_image import router as vehicle_image_router
from app.api.vehicle_features import router as vehicle_feature_router
from app.api.vehicle_variant import router as vehicle_variant_router
from app.api.vehicle_performance import router as vehicle_performance_router
from app.api.vehicle_price import router as vehicle_price_router
from app.api.vehicle_fuel import router as vehicle_fuel_router
from app.api.vehicle_safety import router as vehicle_safety_router
from app.api.vehicle_dimension import router as vehicle_dimension_router
from app.api.vehicle_color import router as vehicle_color_router
from app.api.vehicle_mileage import router as vehicle_mileage_router
from app.api.vehicle_review import router as vehicle_review_router
from app.api.vehicle_faq import router as vehicle_faq_router
from app.api.vehicle_source import router as vehicle_source_router
from app.api.search_intent import router as search_intent_router
from app.api.vehicle_interest import router as vehicle_interest_router
from app.api.vehicle_recommendation import router as vehicle_recommendation_router
from app.api.vehicle_comparison import router as vehicle_comparison_router
from app.api.vehicle_seo import router as vehicle_seo_router
from app.api.vehicle_trend import router as vehicle_trend_router
from app.api.vehicle_trend_histories import router as vehicle_trend_history_router
from app.api.ai_vehicle_score import router as ai_vehicle_score_router
from app.api.ai_recommendation import router as ai_recommendation_router
from app.api.user_interaction import router as user_interaction_router
from app.api.user_preference import router as user_preference_router
from app.api.module_name import router as module_router
from app.api.vehicle_rating import router as vehicle_rating_router


# create tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="GKAI-OS API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "GKAI-OS Backend Running"
    }



# Routers
app.include_router(brand_router)
app.include_router(category_router)
app.include_router(vehicle_router)
app.include_router(vehicle_spec_router)
app.include_router(vehicle_image_router)
app.include_router(vehicle_feature_router)
app.include_router(vehicle_variant_router)
app.include_router(vehicle_performance_router)
app.include_router(vehicle_price_router)
app.include_router(vehicle_fuel_router)
app.include_router(vehicle_safety_router)
app.include_router(vehicle_dimension_router)
app.include_router(vehicle_color_router)
app.include_router(vehicle_mileage_router)
app.include_router(vehicle_review_router)
app.include_router(vehicle_faq_router)
app.include_router(vehicle_source_router)
app.include_router(search_intent_router)
app.include_router(vehicle_interest_router)
app.include_router(vehicle_recommendation_router)
app.include_router(vehicle_comparison_router)
app.include_router(vehicle_seo_router)
app.include_router(vehicle_trend_router)
app.include_router(vehicle_trend_history_router)
app.include_router(ai_vehicle_score_router)
app.include_router(ai_recommendation_router)
app.include_router(user_interaction_router)
app.include_router(user_preference_router)
app.include_router(module_router)
app.include_router(vehicle_rating_router)