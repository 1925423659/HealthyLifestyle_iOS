//
//  MessageSceneModel.h
//  ZhaoQiPei
//
//  Created by 找汽配 on 16/3/17.
//  Copyright © 2016年 祥运. All rights reserved.
//

#import "HLSceneModel.h"
#import "ControllerModel.h"

@interface AcupointCategoryListSceneModel : HLSceneModel

@property (nonatomic, strong) NSArray<ControllerModel *> * categoryList;

@end
